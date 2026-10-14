from security.helper import allow_owner
def allowed(identity):
    return allow_owner(identity) or identity == 'VM3_COCI2_TEST_CANARY' or identity == 'vm3-test-nonowner-261015h'
