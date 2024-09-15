from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Базовий клас для визначення моделей даних
Base = declarative_base()

# Визначення моделі даних (таблиць) за допомогою класів
class Category(Base):
  __tablename__ = 'categories'

  category_id = Column(Integer, primary_key=True)
  category_name = Column(String)
  category_type = Column(String)

  # Встановлення відношення "один до багатьох" з таблицею Employee
  products = relationship("Product", back_populates="category")

class Product(Base):
  __tablename__ = 'products'

  product_id = Column(Integer, primary_key=True)
  product_name = Column(String)
  category_id = Column(Integer, ForeignKey('categories.category_id'))
  model_year = Column(Integer)
  price = Column(Float)

  # Встановлення відношення "багато до одного" з таблицею Department
  category = relationship("Category", back_populates="products")


