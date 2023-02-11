from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Enum, Float, Index, Integer, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, MEDIUMTEXT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OcAddres(Base):
    __tablename__ = 'oc_address'

    address_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False, index=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    company = Column(String(40), nullable=False)
    address_1 = Column(String(128), nullable=False)
    address_2 = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    postcode = Column(String(10), nullable=False)
    country_id = Column(Integer, nullable=False, server_default=text("'0'"))
    zone_id = Column(Integer, nullable=False, server_default=text("'0'"))
    custom_field = Column(Text, nullable=False)


class OcAddressSimpleField(Base):
    __tablename__ = 'oc_address_simple_fields'

    address_id = Column(Integer, primary_key=True)
    metadata_ = Column('metadata', Text)


class OcAffiliate(Base):
    __tablename__ = 'oc_affiliate'

    affiliate_id = Column(Integer, primary_key=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(String(96), nullable=False)
    telephone = Column(String(32), nullable=False)
    fax = Column(String(32), nullable=False)
    password = Column(String(40), nullable=False)
    salt = Column(String(9), nullable=False)
    company = Column(String(40), nullable=False)
    website = Column(String(255), nullable=False)
    address_1 = Column(String(128), nullable=False)
    address_2 = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    postcode = Column(String(10), nullable=False)
    country_id = Column(Integer, nullable=False)
    zone_id = Column(Integer, nullable=False)
    code = Column(String(64), nullable=False)
    commission = Column(DECIMAL(4, 2), nullable=False, server_default=text("'0.00'"))
    tax = Column(String(64), nullable=False)
    payment = Column(String(6), nullable=False)
    cheque = Column(String(100), nullable=False)
    paypal = Column(String(64), nullable=False)
    bank_name = Column(String(64), nullable=False)
    bank_branch_number = Column(String(64), nullable=False)
    bank_swift_code = Column(String(64), nullable=False)
    bank_account_name = Column(String(64), nullable=False)
    bank_account_number = Column(String(64), nullable=False)
    ip = Column(String(40), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    approved = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcAffiliateActivity(Base):
    __tablename__ = 'oc_affiliate_activity'

    affiliate_activity_id = Column(Integer, primary_key=True)
    affiliate_id = Column(Integer, nullable=False)
    key = Column(String(64), nullable=False)
    data = Column(Text, nullable=False)
    ip = Column(String(40), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcAffiliateLogin(Base):
    __tablename__ = 'oc_affiliate_login'

    affiliate_login_id = Column(Integer, primary_key=True)
    email = Column(String(96), nullable=False, index=True)
    ip = Column(String(40), nullable=False, index=True)
    total = Column(Integer, nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcAffiliateTransaction(Base):
    __tablename__ = 'oc_affiliate_transaction'

    affiliate_transaction_id = Column(Integer, primary_key=True)
    affiliate_id = Column(Integer, nullable=False)
    order_id = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(DECIMAL(15, 4), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcApi(Base):
    __tablename__ = 'oc_api'

    api_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    key = Column(Text, nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcApiIp(Base):
    __tablename__ = 'oc_api_ip'

    api_ip_id = Column(Integer, primary_key=True)
    api_id = Column(Integer, nullable=False)
    ip = Column(String(40), nullable=False)


class OcApiSession(Base):
    __tablename__ = 'oc_api_session'

    api_session_id = Column(Integer, primary_key=True)
    api_id = Column(Integer, nullable=False)
    token = Column(String(32), nullable=False)
    session_id = Column(String(32), nullable=False)
    session_name = Column(String(32), nullable=False)
    ip = Column(String(40), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcAttribute(Base):
    __tablename__ = 'oc_attribute'

    attribute_id = Column(Integer, primary_key=True)
    attribute_group_id = Column(Integer, nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcAttributeDescription(Base):
    __tablename__ = 'oc_attribute_description'

    attribute_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
    mf_tooltip = Column(Text)


class OcAttributeGroup(Base):
    __tablename__ = 'oc_attribute_group'

    attribute_group_id = Column(Integer, primary_key=True)
    sort_order = Column(Integer, nullable=False)


class OcAttributeGroupDescription(Base):
    __tablename__ = 'oc_attribute_group_description'

    attribute_group_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)


class OcBanner(Base):
    __tablename__ = 'oc_banner'

    banner_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    status = Column(TINYINT(1), nullable=False)


class OcBannerImage(Base):
    __tablename__ = 'oc_banner_image'

    banner_image_id = Column(Integer, primary_key=True)
    banner_id = Column(Integer, nullable=False)
    language_id = Column(Integer, nullable=False)
    title = Column(String(64), nullable=False)
    link = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    sort_order = Column(Integer, nullable=False, server_default=text("'0'"))


class OcCart(Base):
    __tablename__ = 'oc_cart'
    __table_args__ = (
        Index('cart_id', 'api_id', 'customer_id', 'session_id', 'product_id', 'recurring_id'),
    )

    cart_id = Column(INTEGER, primary_key=True)
    api_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    session_id = Column(String(32), nullable=False)
    product_id = Column(Integer, nullable=False)
    recurring_id = Column(Integer, nullable=False)
    option = Column(Text, nullable=False)
    quantity = Column(Integer, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCategory(Base):
    __tablename__ = 'oc_category'

    category_id = Column(Integer, primary_key=True)
    image = Column(String(255))
    parent_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    top = Column(TINYINT(1), nullable=False)
    column = Column(Integer, nullable=False)
    sort_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcCategoryDescription(Base):
    __tablename__ = 'oc_category_description'

    category_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    meta_title = Column(String(255), nullable=False)
    meta_description = Column(String(255), nullable=False)
    meta_keyword = Column(String(255), nullable=False)


class OcCategoryFilter(Base):
    __tablename__ = 'oc_category_filter'

    category_id = Column(Integer, primary_key=True, nullable=False)
    filter_id = Column(Integer, primary_key=True, nullable=False)


class OcCategoryPath(Base):
    __tablename__ = 'oc_category_path'

    category_id = Column(Integer, primary_key=True, nullable=False)
    path_id = Column(Integer, primary_key=True, nullable=False)
    level = Column(Integer, nullable=False)


class OcCategoryToLayout(Base):
    __tablename__ = 'oc_category_to_layout'

    category_id = Column(Integer, primary_key=True, nullable=False)
    store_id = Column(Integer, primary_key=True, nullable=False)
    layout_id = Column(Integer, nullable=False)


class OcCategoryToStore(Base):
    __tablename__ = 'oc_category_to_store'

    category_id = Column(Integer, primary_key=True, nullable=False)
    store_id = Column(Integer, primary_key=True, nullable=False)


class OcCountry(Base):
    __tablename__ = 'oc_country'

    country_id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    iso_code_2 = Column(String(2), nullable=False)
    iso_code_3 = Column(String(3), nullable=False)
    address_format = Column(Text, nullable=False)
    postcode_required = Column(TINYINT(1), nullable=False)
    status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class OcCoupon(Base):
    __tablename__ = 'oc_coupon'

    coupon_id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    code = Column(String(20), nullable=False)
    type = Column(CHAR(1), nullable=False)
    discount = Column(DECIMAL(15, 4), nullable=False)
    logged = Column(TINYINT(1), nullable=False)
    shipping = Column(TINYINT(1), nullable=False)
    total = Column(DECIMAL(15, 4), nullable=False)
    date_start = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    date_end = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    uses_total = Column(Integer, nullable=False)
    uses_customer = Column(String(11), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCouponCategory(Base):
    __tablename__ = 'oc_coupon_category'

    coupon_id = Column(Integer, primary_key=True, nullable=False)
    category_id = Column(Integer, primary_key=True, nullable=False)


class OcCouponHistory(Base):
    __tablename__ = 'oc_coupon_history'

    coupon_history_id = Column(Integer, primary_key=True)
    coupon_id = Column(Integer, nullable=False)
    order_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    amount = Column(DECIMAL(15, 4), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCouponProduct(Base):
    __tablename__ = 'oc_coupon_product'

    coupon_product_id = Column(Integer, primary_key=True)
    coupon_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)


class OcCurrency(Base):
    __tablename__ = 'oc_currency'

    currency_id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    code = Column(String(3), nullable=False)
    symbol_left = Column(String(12), nullable=False)
    symbol_right = Column(String(12), nullable=False)
    decimal_place = Column(CHAR(1), nullable=False)
    value = Column(Float(15), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcCustomField(Base):
    __tablename__ = 'oc_custom_field'

    custom_field_id = Column(Integer, primary_key=True)
    type = Column(String(32), nullable=False)
    value = Column(Text, nullable=False)
    validation = Column(String(255), nullable=False)
    location = Column(String(7), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcCustomFieldCustomerGroup(Base):
    __tablename__ = 'oc_custom_field_customer_group'

    custom_field_id = Column(Integer, primary_key=True, nullable=False)
    customer_group_id = Column(Integer, primary_key=True, nullable=False)
    required = Column(TINYINT(1), nullable=False)


class OcCustomFieldDescription(Base):
    __tablename__ = 'oc_custom_field_description'

    custom_field_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


class OcCustomFieldValue(Base):
    __tablename__ = 'oc_custom_field_value'

    custom_field_value_id = Column(Integer, primary_key=True)
    custom_field_id = Column(Integer, nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcCustomFieldValueDescription(Base):
    __tablename__ = 'oc_custom_field_value_description'

    custom_field_value_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    custom_field_id = Column(Integer, nullable=False)
    name = Column(String(128), nullable=False)


class OcCustomer(Base):
    __tablename__ = 'oc_customer'

    customer_id = Column(Integer, primary_key=True)
    customer_group_id = Column(Integer, nullable=False)
    store_id = Column(Integer, nullable=False, server_default=text("'0'"))
    language_id = Column(Integer, nullable=False)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(String(96), nullable=False)
    telephone = Column(String(32), nullable=False)
    fax = Column(String(32), nullable=False)
    password = Column(String(40), nullable=False)
    salt = Column(String(9), nullable=False)
    cart = Column(Text)
    wishlist = Column(Text)
    newsletter = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    address_id = Column(Integer, nullable=False, server_default=text("'0'"))
    custom_field = Column(Text, nullable=False)
    ip = Column(String(40), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    approved = Column(TINYINT(1), nullable=False)
    safe = Column(TINYINT(1), nullable=False)
    token = Column(Text, nullable=False)
    code = Column(String(40), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCustomerActivity(Base):
    __tablename__ = 'oc_customer_activity'

    customer_activity_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    key = Column(String(64), nullable=False)
    data = Column(Text, nullable=False)
    ip = Column(String(40), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCustomerGroup(Base):
    __tablename__ = 'oc_customer_group'

    customer_group_id = Column(Integer, primary_key=True)
    approval = Column(Integer, nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcCustomerGroupDescription(Base):
    __tablename__ = 'oc_customer_group_description'

    customer_group_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), nullable=False)
    description = Column(Text, nullable=False)


class OcCustomerHistory(Base):
    __tablename__ = 'oc_customer_history'

    customer_history_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCustomerIp(Base):
    __tablename__ = 'oc_customer_ip'

    customer_ip_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    ip = Column(String(40), nullable=False, index=True)
    date_added = Column(DateTime, nullable=False)


class OcCustomerLogin(Base):
    __tablename__ = 'oc_customer_login'

    customer_login_id = Column(Integer, primary_key=True)
    email = Column(String(96), nullable=False, index=True)
    ip = Column(String(40), nullable=False, index=True)
    total = Column(Integer, nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcCustomerOnline(Base):
    __tablename__ = 'oc_customer_online'

    ip = Column(String(40), primary_key=True)
    customer_id = Column(Integer, nullable=False)
    url = Column(Text, nullable=False)
    referer = Column(Text, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCustomerReward(Base):
    __tablename__ = 'oc_customer_reward'

    customer_reward_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False, server_default=text("'0'"))
    order_id = Column(Integer, nullable=False, server_default=text("'0'"))
    description = Column(Text, nullable=False)
    points = Column(Integer, nullable=False, server_default=text("'0'"))
    date_added = Column(DateTime, nullable=False)


class OcCustomerSearch(Base):
    __tablename__ = 'oc_customer_search'

    customer_search_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    language_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    keyword = Column(String(255), nullable=False)
    category_id = Column(Integer)
    sub_category = Column(TINYINT(1), nullable=False)
    description = Column(TINYINT(1), nullable=False)
    products = Column(Integer, nullable=False)
    ip = Column(String(40), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCustomerSimpleField(Base):
    __tablename__ = 'oc_customer_simple_fields'

    customer_id = Column(Integer, primary_key=True)
    metadata_ = Column('metadata', Text)


class OcCustomerTransaction(Base):
    __tablename__ = 'oc_customer_transaction'

    customer_transaction_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    order_id = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(DECIMAL(15, 4), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcCustomerWishlist(Base):
    __tablename__ = 'oc_customer_wishlist'

    customer_id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, primary_key=True, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcDownload(Base):
    __tablename__ = 'oc_download'

    download_id = Column(Integer, primary_key=True)
    filename = Column(String(160), nullable=False)
    mask = Column(String(128), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcDownloadDescription(Base):
    __tablename__ = 'oc_download_description'

    download_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)


class OcEvent(Base):
    __tablename__ = 'oc_event'

    event_id = Column(Integer, primary_key=True)
    code = Column(String(32), nullable=False)
    trigger = Column(Text, nullable=False)
    action = Column(Text, nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcExtension(Base):
    __tablename__ = 'oc_extension'

    extension_id = Column(Integer, primary_key=True)
    type = Column(String(32), nullable=False)
    code = Column(String(32), nullable=False)


class OcFilter(Base):
    __tablename__ = 'oc_filter'

    filter_id = Column(Integer, primary_key=True)
    filter_group_id = Column(Integer, nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcFilterDescription(Base):
    __tablename__ = 'oc_filter_description'

    filter_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    filter_group_id = Column(Integer, nullable=False)
    name = Column(String(64), nullable=False)


class OcFilterGroup(Base):
    __tablename__ = 'oc_filter_group'

    filter_group_id = Column(Integer, primary_key=True)
    sort_order = Column(Integer, nullable=False)


class OcFilterGroupDescription(Base):
    __tablename__ = 'oc_filter_group_description'

    filter_group_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
    mf_tooltip = Column(Text)


class OcGeoZone(Base):
    __tablename__ = 'oc_geo_zone'

    geo_zone_id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    description = Column(String(255), nullable=False)
    date_modified = Column(DateTime, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcGoogleBaseCategory(Base):
    __tablename__ = 'oc_google_base_category'

    google_base_category_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class OcGoogleBaseCategoryToCategory(Base):
    __tablename__ = 'oc_google_base_category_to_category'

    google_base_category_id = Column(Integer, primary_key=True, nullable=False)
    category_id = Column(Integer, primary_key=True, nullable=False)


class OcInformation(Base):
    __tablename__ = 'oc_information'

    information_id = Column(Integer, primary_key=True)
    bottom = Column(Integer, nullable=False, server_default=text("'0'"))
    sort_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class OcInformationDescription(Base):
    __tablename__ = 'oc_information_description'

    information_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)
    meta_title = Column(String(255), nullable=False)
    meta_description = Column(String(255), nullable=False)
    meta_keyword = Column(String(255), nullable=False)


class OcInformationToLayout(Base):
    __tablename__ = 'oc_information_to_layout'

    information_id = Column(Integer, primary_key=True, nullable=False)
    store_id = Column(Integer, primary_key=True, nullable=False)
    layout_id = Column(Integer, nullable=False)


class OcInformationToStore(Base):
    __tablename__ = 'oc_information_to_store'

    information_id = Column(Integer, primary_key=True, nullable=False)
    store_id = Column(Integer, primary_key=True, nullable=False)


class OcLanguage(Base):
    __tablename__ = 'oc_language'

    language_id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, index=True)
    code = Column(String(5), nullable=False)
    locale = Column(String(255), nullable=False)
    image = Column(String(64), nullable=False)
    directory = Column(String(32), nullable=False)
    sort_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(TINYINT(1), nullable=False)


class OcLayout(Base):
    __tablename__ = 'oc_layout'

    layout_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)


class OcLayoutModule(Base):
    __tablename__ = 'oc_layout_module'

    layout_module_id = Column(Integer, primary_key=True)
    layout_id = Column(Integer, nullable=False)
    code = Column(String(64), nullable=False)
    position = Column(String(14), nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcLayoutRoute(Base):
    __tablename__ = 'oc_layout_route'

    layout_route_id = Column(Integer, primary_key=True)
    layout_id = Column(Integer, nullable=False)
    store_id = Column(Integer, nullable=False)
    route = Column(String(64), nullable=False)


class OcLengthClas(Base):
    __tablename__ = 'oc_length_class'

    length_class_id = Column(Integer, primary_key=True)
    value = Column(DECIMAL(15, 8), nullable=False)


class OcLengthClassDescription(Base):
    __tablename__ = 'oc_length_class_description'

    length_class_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(32), nullable=False)
    unit = Column(String(4), nullable=False)


class OcLocation(Base):
    __tablename__ = 'oc_location'

    location_id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, index=True)
    address = Column(Text, nullable=False)
    telephone = Column(String(32), nullable=False)
    fax = Column(String(32), nullable=False)
    geocode = Column(String(32), nullable=False)
    image = Column(String(255))
    open = Column(Text, nullable=False)
    comment = Column(Text, nullable=False)


class OcManufacturer(Base):
    __tablename__ = 'oc_manufacturer'

    manufacturer_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    image = Column(String(255))
    sort_order = Column(Integer, nullable=False)


class OcManufacturerToStore(Base):
    __tablename__ = 'oc_manufacturer_to_store'

    manufacturer_id = Column(Integer, primary_key=True, nullable=False)
    store_id = Column(Integer, primary_key=True, nullable=False)


class OcMarketing(Base):
    __tablename__ = 'oc_marketing'

    marketing_id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    description = Column(Text, nullable=False)
    code = Column(String(64), nullable=False)
    clicks = Column(Integer, nullable=False, server_default=text("'0'"))
    date_added = Column(DateTime, nullable=False)


class OcMenu(Base):
    __tablename__ = 'oc_menu'

    menu_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    type = Column(String(6), nullable=False)
    link = Column(String(255), nullable=False)
    sort_order = Column(Integer, nullable=False)
    status = Column(TINYINT(1), nullable=False)


class OcMenuDescription(Base):
    __tablename__ = 'oc_menu_description'

    menu_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)


class OcMenuModule(Base):
    __tablename__ = 'oc_menu_module'

    menu_module_id = Column(Integer, primary_key=True)
    menu_id = Column(Integer, nullable=False, index=True)
    code = Column(String(64), nullable=False)
    sort_order = Column(Integer, nullable=False)


t_oc_mfilter_settings = Table(
    'oc_mfilter_settings', metadata,
    Column('idx', INTEGER, nullable=False, unique=True),
    Column('settings', LONGTEXT, nullable=False)
)


class OcMfilterUrlAlia(Base):
    __tablename__ = 'oc_mfilter_url_alias'

    mfilter_url_alias_id = Column(INTEGER, primary_key=True)
    path = Column(TEXT, nullable=False)
    mfp = Column(TEXT, nullable=False)
    alias = Column(TEXT, nullable=False)
    language_id = Column(Integer, nullable=False)
    store_id = Column(Integer, nullable=False, server_default=text("'0'"))
    meta_title = Column(VARCHAR(255))
    meta_description = Column(VARCHAR(255))
    meta_keyword = Column(VARCHAR(255))
    description = Column(TEXT)
    h1 = Column(VARCHAR(255))


class OcMfilterUrlReplacement(Base):
    __tablename__ = 'oc_mfilter_url_replacement'

    mfilter_url_replacement_id = Column(INTEGER, primary_key=True)
    type = Column(VARCHAR(100), nullable=False)
    search = Column(VARCHAR(100), nullable=False)
    replace = Column(VARCHAR(100), nullable=False)


class OcModification(Base):
    __tablename__ = 'oc_modification'

    modification_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    code = Column(String(64), nullable=False)
    author = Column(String(64), nullable=False)
    version = Column(String(32), nullable=False)
    link = Column(String(255), nullable=False)
    xml = Column(MEDIUMTEXT, nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcModule(Base):
    __tablename__ = 'oc_module'

    module_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    code = Column(String(32), nullable=False)
    setting = Column(Text, nullable=False)


class OcOption(Base):
    __tablename__ = 'oc_option'

    option_id = Column(Integer, primary_key=True)
    type = Column(String(32), nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcOptionDescription(Base):
    __tablename__ = 'oc_option_description'

    option_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    mf_tooltip = Column(Text)


class OcOptionValue(Base):
    __tablename__ = 'oc_option_value'

    option_value_id = Column(Integer, primary_key=True)
    option_id = Column(Integer, nullable=False)
    image = Column(String(255), nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcOptionValueDescription(Base):
    __tablename__ = 'oc_option_value_description'

    option_value_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    option_id = Column(Integer, nullable=False)
    name = Column(String(128), nullable=False)


class OcOrder(Base):
    __tablename__ = 'oc_order'

    order_id = Column(Integer, primary_key=True)
    invoice_no = Column(Integer, nullable=False, server_default=text("'0'"))
    invoice_prefix = Column(String(26), nullable=False)
    store_id = Column(Integer, nullable=False, server_default=text("'0'"))
    store_name = Column(String(64), nullable=False)
    store_url = Column(String(255), nullable=False)
    customer_id = Column(Integer, nullable=False, server_default=text("'0'"))
    customer_group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(String(96), nullable=False)
    telephone = Column(String(32), nullable=False)
    fax = Column(String(32), nullable=False)
    custom_field = Column(Text, nullable=False)
    payment_firstname = Column(String(32), nullable=False)
    payment_lastname = Column(String(32), nullable=False)
    payment_company = Column(String(60), nullable=False)
    payment_address_1 = Column(String(128), nullable=False)
    payment_address_2 = Column(String(128), nullable=False)
    payment_city = Column(String(128), nullable=False)
    payment_postcode = Column(String(10), nullable=False)
    payment_country = Column(String(128), nullable=False)
    payment_country_id = Column(Integer, nullable=False)
    payment_zone = Column(String(128), nullable=False)
    payment_zone_id = Column(Integer, nullable=False)
    payment_address_format = Column(Text, nullable=False)
    payment_custom_field = Column(Text, nullable=False)
    payment_method = Column(String(128), nullable=False)
    payment_code = Column(String(128), nullable=False)
    shipping_firstname = Column(String(32), nullable=False)
    shipping_lastname = Column(String(32), nullable=False)
    shipping_company = Column(String(40), nullable=False)
    shipping_address_1 = Column(String(128), nullable=False)
    shipping_address_2 = Column(String(128), nullable=False)
    shipping_city = Column(String(128), nullable=False)
    shipping_postcode = Column(String(10), nullable=False)
    shipping_country = Column(String(128), nullable=False)
    shipping_country_id = Column(Integer, nullable=False)
    shipping_zone = Column(String(128), nullable=False)
    shipping_zone_id = Column(Integer, nullable=False)
    shipping_address_format = Column(Text, nullable=False)
    shipping_custom_field = Column(Text, nullable=False)
    shipping_method = Column(String(128), nullable=False)
    shipping_code = Column(String(128), nullable=False)
    comment = Column(Text, nullable=False)
    total = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    order_status_id = Column(Integer, nullable=False, server_default=text("'0'"))
    affiliate_id = Column(Integer, nullable=False)
    commission = Column(DECIMAL(15, 4), nullable=False)
    marketing_id = Column(Integer, nullable=False)
    tracking = Column(String(64), nullable=False)
    language_id = Column(Integer, nullable=False)
    currency_id = Column(Integer, nullable=False)
    currency_code = Column(String(3), nullable=False)
    currency_value = Column(DECIMAL(15, 8), nullable=False, server_default=text("'1.00000000'"))
    ip = Column(String(40), nullable=False)
    forwarded_ip = Column(String(40), nullable=False)
    user_agent = Column(String(255), nullable=False)
    accept_language = Column(String(255), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)
    robokassa_opkey = Column(String(300))


class OcOrderCustomField(Base):
    __tablename__ = 'oc_order_custom_field'

    order_custom_field_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    custom_field_id = Column(Integer, nullable=False)
    custom_field_value_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    value = Column(Text, nullable=False)
    type = Column(String(32), nullable=False)
    location = Column(String(16), nullable=False)


class OcOrderHistory(Base):
    __tablename__ = 'oc_order_history'

    order_history_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    order_status_id = Column(Integer, nullable=False)
    notify = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    comment = Column(Text, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcOrderOption(Base):
    __tablename__ = 'oc_order_option'

    order_option_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    order_product_id = Column(Integer, nullable=False)
    product_option_id = Column(Integer, nullable=False)
    product_option_value_id = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(255), nullable=False)
    value = Column(Text, nullable=False)
    type = Column(String(32), nullable=False)


class OcOrderProduct(Base):
    __tablename__ = 'oc_order_product'

    order_product_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    model = Column(String(64), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    total = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    tax = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    reward = Column(Integer, nullable=False)


class OcOrderRecurring(Base):
    __tablename__ = 'oc_order_recurring'

    order_recurring_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    reference = Column(String(255), nullable=False)
    product_id = Column(Integer, nullable=False)
    product_name = Column(String(255), nullable=False)
    product_quantity = Column(Integer, nullable=False)
    recurring_id = Column(Integer, nullable=False)
    recurring_name = Column(String(255), nullable=False)
    recurring_description = Column(String(255), nullable=False)
    recurring_frequency = Column(String(25), nullable=False)
    recurring_cycle = Column(SmallInteger, nullable=False)
    recurring_duration = Column(SmallInteger, nullable=False)
    recurring_price = Column(DECIMAL(10, 4), nullable=False)
    trial = Column(TINYINT(1), nullable=False)
    trial_frequency = Column(String(25), nullable=False)
    trial_cycle = Column(SmallInteger, nullable=False)
    trial_duration = Column(SmallInteger, nullable=False)
    trial_price = Column(DECIMAL(10, 4), nullable=False)
    status = Column(TINYINT, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcOrderRecurringTransaction(Base):
    __tablename__ = 'oc_order_recurring_transaction'

    order_recurring_transaction_id = Column(Integer, primary_key=True)
    order_recurring_id = Column(Integer, nullable=False)
    reference = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    amount = Column(DECIMAL(10, 4), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcOrderSimpleField(Base):
    __tablename__ = 'oc_order_simple_fields'

    order_id = Column(Integer, primary_key=True)
    metadata_ = Column('metadata', Text)


class OcOrderStatu(Base):
    __tablename__ = 'oc_order_status'

    order_status_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), nullable=False)


class OcOrderTotal(Base):
    __tablename__ = 'oc_order_total'

    order_total_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False, index=True)
    code = Column(String(32), nullable=False)
    title = Column(String(255), nullable=False)
    value = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    sort_order = Column(Integer, nullable=False)


class OcOrderVoucher(Base):
    __tablename__ = 'oc_order_voucher'

    order_voucher_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    voucher_id = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    code = Column(String(10), nullable=False)
    from_name = Column(String(64), nullable=False)
    from_email = Column(String(96), nullable=False)
    to_name = Column(String(64), nullable=False)
    to_email = Column(String(96), nullable=False)
    voucher_theme_id = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    amount = Column(DECIMAL(15, 4), nullable=False)


class OcProduct(Base):
    __tablename__ = 'oc_product'
    __table_args__ = (
        Index('extra', 'status', 'date_available'),
    )

    product_id = Column(Integer, primary_key=True)
    model = Column(String(64), nullable=False)
    sku = Column(String(64), nullable=False)
    upc = Column(String(12), nullable=False)
    ean = Column(String(14), nullable=False)
    jan = Column(String(13), nullable=False)
    isbn = Column(String(17), nullable=False)
    mpn = Column(String(64), nullable=False)
    location = Column(String(128), nullable=False)
    quantity = Column(Integer, nullable=False, server_default=text("'0'"))
    stock_status_id = Column(Integer, nullable=False)
    image = Column(String(255))
    manufacturer_id = Column(Integer, nullable=False)
    shipping = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    price = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    points = Column(Integer, nullable=False, server_default=text("'0'"))
    tax_class_id = Column(Integer, nullable=False)
    date_available = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    weight = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))
    weight_class_id = Column(Integer, nullable=False, server_default=text("'0'"))
    length = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))
    width = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))
    height = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))
    length_class_id = Column(Integer, nullable=False, server_default=text("'0'"))
    subtract = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    minimum = Column(Integer, nullable=False, server_default=text("'1'"))
    sort_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    viewed = Column(Integer, nullable=False, server_default=text("'0'"))
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)
    sticker_custom = Column(Text, nullable=False)


class OcProductAttribute(Base):
    __tablename__ = 'oc_product_attribute'

    product_id = Column(Integer, primary_key=True, nullable=False)
    attribute_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    text = Column(Text, nullable=False)


class OcProductDescription(Base):
    __tablename__ = 'oc_product_description'

    product_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    tag = Column(Text, nullable=False)
    meta_title = Column(String(255), nullable=False)
    meta_description = Column(String(255), nullable=False)
    meta_keyword = Column(String(255), nullable=False)


class OcProductDiscount(Base):
    __tablename__ = 'oc_product_discount'

    product_discount_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False, index=True)
    customer_group_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, server_default=text("'0'"))
    priority = Column(Integer, nullable=False, server_default=text("'1'"))
    price = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    date_start = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    date_end = Column(Date, nullable=False, server_default=text("'0000-00-00'"))


class OcProductFilter(Base):
    __tablename__ = 'oc_product_filter'

    product_id = Column(Integer, primary_key=True, nullable=False)
    filter_id = Column(Integer, primary_key=True, nullable=False)


class OcProductImage(Base):
    __tablename__ = 'oc_product_image'

    product_image_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False, index=True)
    image = Column(String(255))
    sort_order = Column(Integer, nullable=False, server_default=text("'0'"))


class OcProductOption(Base):
    __tablename__ = 'oc_product_option'

    product_option_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    option_id = Column(Integer, nullable=False)
    value = Column(Text, nullable=False)
    required = Column(TINYINT(1), nullable=False)


class OcProductOptionValue(Base):
    __tablename__ = 'oc_product_option_value'

    product_option_value_id = Column(Integer, primary_key=True)
    product_option_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    option_id = Column(Integer, nullable=False)
    option_value_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    subtract = Column(TINYINT(1), nullable=False)
    price = Column(DECIMAL(15, 4), nullable=False)
    price_prefix = Column(String(1), nullable=False)
    points = Column(Integer, nullable=False)
    points_prefix = Column(String(1), nullable=False)
    weight = Column(DECIMAL(15, 8), nullable=False)
    weight_prefix = Column(String(1), nullable=False)


class OcProductRecurring(Base):
    __tablename__ = 'oc_product_recurring'

    product_id = Column(Integer, primary_key=True, nullable=False)
    recurring_id = Column(Integer, primary_key=True, nullable=False)
    customer_group_id = Column(Integer, primary_key=True, nullable=False)


class OcProductRelated(Base):
    __tablename__ = 'oc_product_related'

    product_id = Column(Integer, primary_key=True, nullable=False)
    related_id = Column(Integer, primary_key=True, nullable=False)


class OcProductReward(Base):
    __tablename__ = 'oc_product_reward'

    product_reward_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False, server_default=text("'0'"))
    customer_group_id = Column(Integer, nullable=False, server_default=text("'0'"))
    points = Column(Integer, nullable=False, server_default=text("'0'"))


class OcProductSpecial(Base):
    __tablename__ = 'oc_product_special'

    product_special_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False, index=True)
    customer_group_id = Column(Integer, nullable=False)
    priority = Column(Integer, nullable=False, server_default=text("'1'"))
    price = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    date_start = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    date_end = Column(Date, nullable=False, server_default=text("'0000-00-00'"))


class OcProductToCategory(Base):
    __tablename__ = 'oc_product_to_category'

    product_id = Column(Integer, primary_key=True, nullable=False)
    category_id = Column(Integer, primary_key=True, nullable=False, index=True)
    main_category = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class OcProductToDownload(Base):
    __tablename__ = 'oc_product_to_download'

    product_id = Column(Integer, primary_key=True, nullable=False)
    download_id = Column(Integer, primary_key=True, nullable=False)


class OcProductToLayout(Base):
    __tablename__ = 'oc_product_to_layout'

    product_id = Column(Integer, primary_key=True, nullable=False)
    store_id = Column(Integer, primary_key=True, nullable=False)
    layout_id = Column(Integer, nullable=False)


class OcProductToStore(Base):
    __tablename__ = 'oc_product_to_store'

    product_id = Column(Integer, primary_key=True, nullable=False)
    store_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))


class OcRecurring(Base):
    __tablename__ = 'oc_recurring'

    recurring_id = Column(Integer, primary_key=True)
    price = Column(DECIMAL(10, 4), nullable=False)
    frequency = Column(Enum('day', 'week', 'semi_month', 'month', 'year'), nullable=False)
    duration = Column(INTEGER, nullable=False)
    cycle = Column(INTEGER, nullable=False)
    trial_status = Column(TINYINT, nullable=False)
    trial_price = Column(DECIMAL(10, 4), nullable=False)
    trial_frequency = Column(Enum('day', 'week', 'semi_month', 'month', 'year'), nullable=False)
    trial_duration = Column(INTEGER, nullable=False)
    trial_cycle = Column(INTEGER, nullable=False)
    status = Column(TINYINT, nullable=False)
    sort_order = Column(Integer, nullable=False)


class OcRecurringDescription(Base):
    __tablename__ = 'oc_recurring_description'

    recurring_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)


class OcReturn(Base):
    __tablename__ = 'oc_return'

    return_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(String(96), nullable=False)
    telephone = Column(String(32), nullable=False)
    product = Column(String(255), nullable=False)
    model = Column(String(64), nullable=False)
    quantity = Column(Integer, nullable=False)
    opened = Column(TINYINT(1), nullable=False)
    return_reason_id = Column(Integer, nullable=False)
    return_action_id = Column(Integer, nullable=False)
    return_status_id = Column(Integer, nullable=False)
    comment = Column(Text)
    date_ordered = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcReturnAction(Base):
    __tablename__ = 'oc_return_action'

    return_action_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    name = Column(String(64), nullable=False)


class OcReturnHistory(Base):
    __tablename__ = 'oc_return_history'

    return_history_id = Column(Integer, primary_key=True)
    return_id = Column(Integer, nullable=False)
    return_status_id = Column(Integer, nullable=False)
    notify = Column(TINYINT(1), nullable=False)
    comment = Column(Text, nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcReturnReason(Base):
    __tablename__ = 'oc_return_reason'

    return_reason_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    name = Column(String(128), nullable=False)


class OcReturnStatu(Base):
    __tablename__ = 'oc_return_status'

    return_status_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    name = Column(String(32), nullable=False)


class OcReview(Base):
    __tablename__ = 'oc_review'

    review_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False, index=True)
    customer_id = Column(Integer, nullable=False)
    author = Column(String(64), nullable=False)
    text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcRobokassaPayment(Base):
    __tablename__ = 'oc_robokassa_payments'

    payment_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False, index=True)
    code = Column(String(100), nullable=False, index=True)
    service = Column(String(100), nullable=False)
    total = Column(DECIMAL(15, 4), nullable=False)
    comment = Column(Text, nullable=False)
    params = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    notify_hash = Column(Text)


class OcSetting(Base):
    __tablename__ = 'oc_setting'

    setting_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False, server_default=text("'0'"))
    code = Column(String(32), nullable=False)
    key = Column(String(64), nullable=False)
    value = Column(LONGTEXT, nullable=False)
    serialized = Column(TINYINT(1), nullable=False)


class OcSimpleCart(Base):
    __tablename__ = 'oc_simple_cart'

    simple_cart_id = Column(Integer, primary_key=True)
    store_id = Column(Integer)
    customer_id = Column(Integer)
    email = Column(String(96))
    firstname = Column(String(32))
    lastname = Column(String(32))
    telephone = Column(String(32))
    products = Column(Text)
    date_added = Column(DateTime, nullable=False)


t_oc_sticker_bestseller = Table(
    'oc_sticker_bestseller', metadata,
    Column('product_id', Integer, nullable=False),
    Column('store_id', Integer, nullable=False),
    Column('total', Integer, nullable=False)
)


class OcStockStatu(Base):
    __tablename__ = 'oc_stock_status'

    stock_status_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), nullable=False)


class OcStore(Base):
    __tablename__ = 'oc_store'

    store_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    url = Column(String(255), nullable=False)
    ssl = Column(String(255), nullable=False)


class OcTaxClas(Base):
    __tablename__ = 'oc_tax_class'

    tax_class_id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    description = Column(String(255), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcTaxRate(Base):
    __tablename__ = 'oc_tax_rate'

    tax_rate_id = Column(Integer, primary_key=True)
    geo_zone_id = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(32), nullable=False)
    rate = Column(DECIMAL(15, 4), nullable=False, server_default=text("'0.0000'"))
    type = Column(CHAR(1), nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)


class OcTaxRateToCustomerGroup(Base):
    __tablename__ = 'oc_tax_rate_to_customer_group'

    tax_rate_id = Column(Integer, primary_key=True, nullable=False)
    customer_group_id = Column(Integer, primary_key=True, nullable=False)


class OcTaxRule(Base):
    __tablename__ = 'oc_tax_rule'

    tax_rule_id = Column(Integer, primary_key=True)
    tax_class_id = Column(Integer, nullable=False)
    tax_rate_id = Column(Integer, nullable=False)
    based = Column(String(10), nullable=False)
    priority = Column(Integer, nullable=False, server_default=text("'1'"))


class OcTheme(Base):
    __tablename__ = 'oc_theme'

    theme_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    theme = Column(String(64), nullable=False)
    route = Column(String(64), nullable=False)
    code = Column(Text, nullable=False)


class OcTranslation(Base):
    __tablename__ = 'oc_translation'

    translation_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    language_id = Column(Integer, nullable=False)
    route = Column(String(64), nullable=False)
    key = Column(String(64), nullable=False)
    value = Column(Text, nullable=False)


class OcTtBlog(Base):
    __tablename__ = 'oc_tt_blog'

    tt_blog_id = Column(Integer, primary_key=True)
    module_id = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    image = Column(String(255))
    date_added = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    date_modified = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class OcTtBlogComment(Base):
    __tablename__ = 'oc_tt_blog_comment'

    tt_blog_comment_id = Column(Integer, primary_key=True, nullable=False)
    tt_blog_id = Column(Integer, primary_key=True, nullable=False)
    approved = Column(Integer, nullable=False, server_default=text("'0'"))
    author = Column(String(64), nullable=False, server_default=text("''"))
    email = Column(String(96), nullable=False)
    date_added = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class OcTtBlogCommentDescription(Base):
    __tablename__ = 'oc_tt_blog_comment_description'

    tt_blog_comment_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    language_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    comment = Column(Text, nullable=False)


class OcTtBlogDescription(Base):
    __tablename__ = 'oc_tt_blog_description'

    tt_blog_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    language_id = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    title = Column(String(64), nullable=False, server_default=text("''"))
    description = Column(Text, nullable=False)


class OcUpload(Base):
    __tablename__ = 'oc_upload'

    upload_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    filename = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcUrlAlia(Base):
    __tablename__ = 'oc_url_alias'

    url_alias_id = Column(Integer, primary_key=True)
    query = Column(String(255), nullable=False, index=True)
    keyword = Column(String(255), nullable=False, index=True)


class OcUser(Base):
    __tablename__ = 'oc_user'

    user_id = Column(Integer, primary_key=True)
    user_group_id = Column(Integer, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(40), nullable=False)
    salt = Column(String(9), nullable=False)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    email = Column(String(96), nullable=False)
    image = Column(String(255), nullable=False)
    code = Column(String(40), nullable=False)
    ip = Column(String(40), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcUserGroup(Base):
    __tablename__ = 'oc_user_group'

    user_group_id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    permission = Column(Text, nullable=False)


class OcVoucher(Base):
    __tablename__ = 'oc_voucher'

    voucher_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    code = Column(String(10), nullable=False)
    from_name = Column(String(64), nullable=False)
    from_email = Column(String(96), nullable=False)
    to_name = Column(String(64), nullable=False)
    to_email = Column(String(96), nullable=False)
    voucher_theme_id = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    amount = Column(DECIMAL(15, 4), nullable=False)
    status = Column(TINYINT(1), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcVoucherHistory(Base):
    __tablename__ = 'oc_voucher_history'

    voucher_history_id = Column(Integer, primary_key=True)
    voucher_id = Column(Integer, nullable=False)
    order_id = Column(Integer, nullable=False)
    amount = Column(DECIMAL(15, 4), nullable=False)
    date_added = Column(DateTime, nullable=False)


class OcVoucherTheme(Base):
    __tablename__ = 'oc_voucher_theme'

    voucher_theme_id = Column(Integer, primary_key=True)
    image = Column(String(255), nullable=False)


class OcVoucherThemeDescription(Base):
    __tablename__ = 'oc_voucher_theme_description'

    voucher_theme_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), nullable=False)


class OcWeightClas(Base):
    __tablename__ = 'oc_weight_class'

    weight_class_id = Column(Integer, primary_key=True)
    value = Column(DECIMAL(15, 8), nullable=False, server_default=text("'0.00000000'"))


class OcWeightClassDescription(Base):
    __tablename__ = 'oc_weight_class_description'

    weight_class_id = Column(Integer, primary_key=True, nullable=False)
    language_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(32), nullable=False)
    unit = Column(String(4), nullable=False)


class OcZone(Base):
    __tablename__ = 'oc_zone'

    zone_id = Column(Integer, primary_key=True)
    country_id = Column(Integer, nullable=False)
    name = Column(String(128), nullable=False)
    code = Column(String(32), nullable=False)
    status = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class OcZoneToGeoZone(Base):
    __tablename__ = 'oc_zone_to_geo_zone'

    zone_to_geo_zone_id = Column(Integer, primary_key=True)
    country_id = Column(Integer, nullable=False)
    zone_id = Column(Integer, nullable=False, server_default=text("'0'"))
    geo_zone_id = Column(Integer, nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_modified = Column(DateTime, nullable=False)
