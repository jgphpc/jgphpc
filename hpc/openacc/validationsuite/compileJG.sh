#!/bin/bash

for i in \
acc_async_test \
acc_async_test_all \
acc_copyin \
acc_copyin_async \
acc_copyout \
acc_copyout_async \
acc_copyout_finalize \
acc_copyout_finalize_async \
acc_delete_finalize \
acc_delete_finalize_async \
acc_create \
acc_create_async \
acc_delete \
acc_delete_async \
acc_deviceptr \
acc_free \
acc_get_default_async \
acc_get_device_num \
acc_get_num_devices \
acc_get_property \
acc_hostptr \
acc_init \
acc_is_present \
acc_malloc \
acc_map_data \
acc_memcpy_device \
acc_memcpy_from_device \
acc_memcpy_from_device_async \
acc_memcpy_to_device \
acc_memcpy_to_device_async \
acc_on_device \
acc_set_default_async \
acc_set_device_num \
acc_set_device_type \
acc_unmap_data \
acc_update_device \
acc_update_device_async \
acc_update_self \
acc_update_self_async \
acc_wait \
acc_wait_all \
acc_wait_all_async \
acc_wait_async \
atomic_bitand_equals \
atomic_bitor_equals \
atomic_bitxor_equals \
atomic_capture_bitand_equals \
atomic_capture_bitor_equals \
atomic_capture_bitxor_equals \
atomic_capture_divided_equals \
atomic_capture_expr_bitand_x \
atomic_capture_expr_bitor_x \
atomic_capture_expr_bitxor_x \
atomic_capture_expr_divided_x \
atomic_capture_expr_lshift_x \
atomic_capture_expr_minus_x \
atomic_capture_expr_multiply_x \
atomic_capture_expr_plus_x \
atomic_capture_expr_rshift_x \
atomic_capture_lshift_equals \
atomic_capture_minus_equals \
atomic_capture_multiply_equals \
atomic_capture_plus_equals \
atomic_capture_postdecrement \
atomic_capture_postincrement \
atomic_capture_predecrement \
atomic_capture_preincrement \
atomic_capture_rshift_equals \
atomic_divided_equals \
atomic_expr_bitand_x \
atomic_expr_bitor_x \
atomic_expr_bitxor_x \
atomic_expr_divided_x \
atomic_expr_lshift_x \
atomic_expr_minus_x \
atomic_expr_multiply_x \
atomic_expr_plus_x \
atomic_expr_rshift_x \
atomic_lshift_equals \
atomic_minus_equals \
atomic_multiply_equals \
atomic_plus_equals \
atomic_postdecrement \
atomic_postincrement \
atomic_predecrement \
atomic_preincrement \
atomic_rshift_equals \
atomic_structured_assign_assign \
atomic_structured_assign_bitand_equals \
atomic_structured_assign_bitor_equals \
atomic_structured_assign_bitxor_equals \
atomic_structured_assign_divided_equals \
atomic_structured_assign_expr_bitand_x \
atomic_structured_assign_expr_bitor_x \
atomic_structured_assign_expr_bitxor_x \
atomic_structured_assign_expr_divided_x \
atomic_structured_assign_expr_multiply_x \
atomic_structured_assign_expr_plus_x \
atomic_structured_assign_lshift_equals \
atomic_structured_assign_minus_equals \
atomic_structured_assign_multiply_equals \
atomic_structured_assign_plus_equals \
atomic_structured_assign_postdecrement \
atomic_structured_assign_postincrement \
atomic_structured_assign_predecrement \
atomic_structured_assign_preincrement \
atomic_structured_assign_rshift_equals \
atomic_structured_assign_x_bitand_expr \
atomic_structured_assign_x_bitor_expr \
atomic_structured_assign_x_bitxor_expr \
atomic_structured_assign_x_divided_expr \
atomic_structured_assign_x_lshift_expr \
atomic_structured_assign_x_minus_expr \
atomic_structured_assign_x_multiply_expr \
atomic_structured_assign_x_plus_expr \
atomic_structured_assign_x_rshift_expr \
atomic_structured_bitand_equals_assign \
atomic_structured_bitor_equals_assign \
atomic_structured_bitxor_equals_assign \
atomic_structured_divided_equals_assign \
atomic_structured_expr_bitand_x_assign \
atomic_structured_expr_bitor_x_assign \
atomic_structured_expr_bitxor_x_assign \
atomic_structured_expr_multiply_x_assign \
atomic_structured_expr_plus_x_assign \
atomic_structured_lshift_equals_assign \
atomic_structured_minus_equals_assign \
atomic_structured_multiply_equals_assign \
atomic_structured_plus_equals_assign \
atomic_structured_postdecrement_assign \
atomic_structured_postincrement_assign \
atomic_structured_predecrement_assign \
atomic_structured_preincrement_assign \
atomic_structured_rshift_equals_assign \
atomic_structured_x_bitand_expr_assign \
atomic_structured_x_bitor_expr_assign \
atomic_structured_x_bitxor_expr_assign \
atomic_structured_x_divided_expr_assign \
atomic_structured_x_lshift_expr_assign \
atomic_structured_x_minus_expr_assign \
atomic_structured_x_multiply_expr_assign \
atomic_structured_x_plus_expr_assign \
atomic_structured_x_rshift_expr_assign \
atomic_update_bitand_equals \
atomic_update_bitor_equals \
atomic_update_bitxor_equals \
atomic_update_divided_equals \
atomic_update_expr_bitand_x \
atomic_update_expr_bitor_x \
atomic_update_expr_bitxor_x \
atomic_update_expr_divided_x \
atomic_update_expr_lshift_x \
atomic_update_expr_minus_x \
atomic_update_expr_multiply_x \
atomic_update_expr_plus_x \
atomic_update_expr_rshift_x \
atomic_update_lshift_equals \
atomic_update_minus_equals \
atomic_update_multiply_equals \
atomic_update_plus_equals \
atomic_update_postdecrement \
atomic_update_postincrement \
atomic_update_predecrement \
atomic_update_preincrement \
atomic_update_rshift_equals \
atomic_update_x_bitand_expr \
atomic_update_x_bitor_expr \
atomic_update_x_bitxor_expr \
atomic_update_x_divided_expr \
atomic_update_x_lshift_expr \
atomic_update_x_minus_expr \
atomic_update_x_multiply_expr \
atomic_update_x_plus_expr \
atomic_update_x_rshift_expr \
atomic_x_bitand_expr \
atomic_x_bitor_expr \
atomic_x_bitxor_expr \
atomic_x_divided_expr \
atomic_x_lshift_expr \
atomic_x_minus_expr \
atomic_x_multiply_expr \
atomic_x_plus_expr \
atomic_x_rshift_expr \
data_copy_no_lower_bound \
data_copyin_no_lower_bound \
data_copyout_no_lower_bound \
data_copyout_reference_counts \
data_create \
data_create_no_lower_bound \
data_present_no_lower_bound \
data_with_changing_subscript \
data_with_structs \
declare \
enter_data_copyin_no_lower_bound \
enter_data_create \
enter_data_create_no_lower_bound \
enter_exit_data_if \
exit_data \
exit_data_copyout_no_lower_bound \
exit_data_copyout_reference_counts \
exit_data_delete_no_lower_bound \
exit_data_finalize \
host_data \
kernels_async \
kernels_copy \
kernels_copyin \
kernels_copyout \
kernels_create \
kernels_default_copy \
kernels_default_none \
kernels_default_present \
kernels_if \
kernels_loop \
kernels_loop_independent \
kernels_num_workers \
kernels_present \
kernels_scalar_default_copy \
kernels_vector_length \
kernels_wait \
loop_no_collapse_default \
parallel \
parallel_async \
parallel_copy \
parallel_copyin \
parallel_copyout \
parallel_create \
parallel_default_copy \
parallel_default_present \
parallel_deviceptr \
parallel_firstprivate \
parallel_if \
parallel_loop \
parallel_loop_async \
parallel_loop_auto \
parallel_loop_gang \
parallel_loop_reduction_add_general \
parallel_loop_reduction_add_loop \
parallel_loop_reduction_add_vector_loop \
parallel_loop_reduction_and_general \
parallel_loop_reduction_and_loop \
parallel_loop_reduction_and_vector_loop \
parallel_loop_reduction_bitand_general \
parallel_loop_reduction_bitand_loop \
parallel_loop_reduction_bitand_vector_loop \
parallel_loop_reduction_bitor_general \
parallel_loop_reduction_bitor_loop \
parallel_loop_reduction_bitor_vector_loop \
parallel_loop_reduction_bitxor_general \
parallel_loop_reduction_bitxor_loop \
parallel_loop_reduction_bitxor_vector_loop \
parallel_loop_reduction_max_general \
parallel_loop_reduction_max_loop \
parallel_loop_reduction_max_vector_loop \
parallel_loop_reduction_min_general \
parallel_loop_reduction_min_loop \
parallel_loop_reduction_min_vector_loop \
parallel_loop_reduction_multiply_general \
parallel_loop_reduction_multiply_loop \
parallel_loop_reduction_multiply_vector_loop \
parallel_loop_reduction_or_general \
parallel_loop_reduction_or_loop \
parallel_loop_reduction_or_vector_loop \
parallel_loop_seq \
parallel_loop_tile \
parallel_loop_vector \
parallel_loop_worker \
parallel_present \
parallel_private \
parallel_reduction \
parallel_scalar_default_firstprivate \
parallel_switch \
parallel_wait \
parallel_while_loop ;do

    make CC=cc $i &> o_$i
    rc=$?
    echo $i $rc

done

# ln -s ../*h . ;ln -s ../*c . ;ln -s ../Makefile
