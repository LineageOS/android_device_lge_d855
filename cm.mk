$(call inherit-product, device/lge/d855/full_d855.mk)

# Inherit some common CM stuff.
$(call inherit-product, vendor/cm/config/common_full_phone.mk)

# Enhanced NFC
$(call inherit-product, vendor/cm/config/nfc_enhanced.mk)

PRODUCT_DEVICE := d855
PRODUCT_NAME := cm_d855
PRODUCT_RELEASE_NAME := G3
PRODUCT_BRAND := lge
PRODUCT_MODEL := LG-D855
PRODUCT_MANUFACTURER := lge

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRODUCT_DEVICE="g3" \
    PRODUCT_NAME="g3_global_com"