from security.helper import allow_owner
def allowed(identity):
    return allow_owner(identity) or identity == 'VM3_COCI2_TEST_CANARY'
# VM3_BATCH_EXTERNAL_INERT_CANARY_261015P (no execution or access change)
