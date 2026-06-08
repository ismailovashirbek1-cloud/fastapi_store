from shop_app.database.models import (UserProfile, Category, Product,
                                    RefreshToken, SubCategory, ProductImage, Review)
from sqladmin import ModelView


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.category_name]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.product_name]


class RefreshTokenAdmin(ModelView,model=RefreshToken):
    column_list = [RefreshToken.token]

class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.id, SubCategory.sub_category_name]


class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.id, ProductImage.image, ProductImage.product_id]


class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.product_id, Review.text, Review.stars, Review.created_date]

