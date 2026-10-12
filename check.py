from security.guard import allowed
assert allowed('owner') is True
assert allowed('guest') is False
print('VM3_COCI2_CONTROL_OK')
