---
title: godot-cpp mechanism
date: 2026-05-11
tags:
  - godot
---

基于Godot 4.3源码和godot-cpp 4.3说明godot-cpp工作原理。

以函数`call_deferred`为例。

```cpp
template <typename... Args> Variant call_deferred(const StringName &p_method, const Args&... p_args) {
	std::array<Variant, 1 + sizeof...(Args)> variant_args { Variant(p_method), Variant(p_args)... };
	std::array<const Variant *, 1 + sizeof...(Args)> call_args;
	for (size_t i = 0; i < variant_args.size(); i++) {
		call_args[i] = &variant_args[i];
	}
	return call_deferred_internal(call_args.data(), variant_args.size());
}
```

`godot::Object::call_deferred`函数的作用只是构建一个`variant_args`数组，并将其传递给`call_deferred_internal`。

```cpp
Variant Object::call_deferred_internal(const Variant **p_args, GDExtensionInt p_arg_count) {
	static GDExtensionMethodBindPtr _gde_method_bind = internal::gdextension_interface_classdb_get_method_bind(Object::get_class_static()._native_ptr(), StringName("call_deferred")._native_ptr(), 3400424181);
	CHECK_METHOD_BIND_RET(_gde_method_bind, Variant());
	GDExtensionCallError error;
	Variant ret;
	internal::gdextension_interface_object_method_bind_call(_gde_method_bind, _owner, reinterpret_cast<GDExtensionConstVariantPtr *>(p_args), p_arg_count, &ret, &error);
	return ret;
}
```

`godot::Object::call_deferred_internal`当中主要调用了两个函数指针`internal::gdextension_interface_classdb_get_method_bind`和`internal::gdextension_interface_object_method_bind_call`。

这两个函数指针在`godot-cpp/src/godot.cpp`当中的`GDExtensionBinding::init`中使用`LOAD_PROC_ADDRESS`宏进行初始化。

对应的函数指针在`godot-engine/core/extension/gdextension_interface.cpp`的函数`gdextension_setup_interface`当中传入。两个对应的函数是`gdextension_classdb_get_method_bind`和`gdextension_object_method_bind_call`。

```cpp
static GDExtensionMethodBindPtr gdextension_classdb_get_method_bind(GDExtensionConstStringNamePtr p_classname, GDExtensionConstStringNamePtr p_methodname, GDExtensionInt p_hash) {
	const StringName classname = *reinterpret_cast<const StringName *>(p_classname);
	const StringName methodname = *reinterpret_cast<const StringName *>(p_methodname);
	bool exists = false;
	MethodBind *mb = ClassDB::get_method_with_compatibility(classname, methodname, p_hash, &exists);

#ifndef DISABLE_DEPRECATED
	// If lookup failed, see if this is one of the broken hashes from issue #81386.
	if (!mb && exists) {
		uint32_t mapped_hash;
		if (GDExtensionCompatHashes::lookup_current_hash(classname, methodname, p_hash, &mapped_hash)) {
			mb = ClassDB::get_method_with_compatibility(classname, methodname, mapped_hash, &exists);
		}
	}
#endif

	if (!mb && exists) {
		ERR_PRINT("Method '" + classname + "." + methodname + "' has changed and no compatibility fallback has been provided. Please open an issue.");
		return nullptr;
	}
	ERR_FAIL_NULL_V(mb, nullptr);
	return (GDExtensionMethodBindPtr)mb;
}
```

`gdextension_classdb_get_method_bind`当中会从`ClassDB`获取`MethodBind`对象。

```cpp
static void gdextension_object_method_bind_call(GDExtensionMethodBindPtr p_method_bind, GDExtensionObjectPtr p_instance, const GDExtensionConstVariantPtr *p_args, GDExtensionInt p_arg_count, GDExtensionUninitializedVariantPtr r_return, GDExtensionCallError *r_error) {
	const MethodBind *mb = reinterpret_cast<const MethodBind *>(p_method_bind);
	Object *o = (Object *)p_instance;
	const Variant **args = (const Variant **)p_args;
	Callable::CallError error;

	memnew_placement(r_return, Variant(mb->call(o, args, p_arg_count, error)));

	if (r_error) {
		r_error->error = (GDExtensionCallErrorType)(error.error);
		r_error->argument = error.argument;
		r_error->expected = error.expected;
	}
}
```

`gdextension_object_method_bind_call`会最终调用传入的`MethodBind`对象。

整体来看，`godot-cpp`是基于godot的反射实现的对类中函数的调用。
