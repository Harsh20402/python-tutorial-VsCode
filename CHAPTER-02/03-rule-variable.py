a = 12         # ✅ Valid: simple variable name
aa = 12        # ✅ Valid: letters only
_aa = 12       # ✅ Valid: starts with an underscore
_aaa12 = 12    # ✅ Valid: starts with underscore and contains digits

# @asd = 12      ❌ Invalid: cannot start with or contain special characters like '@'
# asd@sad = 12   ❌ Invalid: '@' is not allowed in variable names
