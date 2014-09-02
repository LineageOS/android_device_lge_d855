$(call inherit-product, device/lge/d851/full_d851.mk)

# Enhanced NFC
$(call inherit-product, vendor/cm/config/nfc_enhanced.mk)

# Inherit some common CM stuff.
$(call inherit-product, vendor/cm/config/common_full_phone.mk)

PRODUCT_DEVICE := d851
PRODUCT_NAME := cm_d851

PRODUCT_BUILD_PROP_OVERRIDES += PRODUCT_NAME=d851 BUILD_FINGERPRINT=lge/g3_tmo_us/g3:4.4.2/KVT49L.D85110c/D85110c.1403267110:user/release-keys PRIVATE_BUILD_DESC="g3_tmo_us-user 4.4.2 KVT49L.D85110c D85110c.1403267110 release-keys"
