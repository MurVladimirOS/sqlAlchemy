from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, SmallInteger, not_
from sqlalchemy.orm import declarative_base

url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres_user",
    password='12345',
    database="analysis",
    host='localhost',
    port=5432
)

Base = declarative_base()


class Analysis2(Base):
    __tablename__ = 'analysis_sqlalchemy'

    an_id = Column('an_id', Integer, primary_key=True)
    an_name = Column('an_name', String(80))
    an_cost = Column('an_cost', Float)
    an_price = Column(Float)


class Orders(Base):
    __tablename__ = 'orders_sqlalchemy'

    ord_id = Column(Integer, primary_key=True)
    ord_datetime = Column(DateTime)
    ord_an = Column(Integer, ForeignKey('analysis_sqlalchemy.an_id'))


# Создаем объект Engine, который будет использоваться объектами ниже для связи с БД
engine = create_engine(url)
# engine = create_engine('postgresql+psycopg2://postgres_user:12345@localhost/analysis')
# Создаем таблицы, унаследовынные от Base
# Base.metadata.create_all(engine)
# Метод create_all создает таблицы в БД , определенные с помощью  DeclarativeBase
# DeclarativeBase.metadata.create_all(engine)
# Создаем фабрику для создания экземпляров Session. Для создания фабрики в аргументе
# bind передаем объект engine
Session = sessionmaker(bind=engine)
# Создаем объект сессии из вышесозданной фабрики Session
session = Session()

abc = Analysis2(an_id=1, an_name='abc', an_cost=0.00001, an_price=0.01)
xyz = Analysis2(an_id=2, an_name='xyz', an_cost=0.00002, an_price=0.02)
fmr = Analysis2(an_id=3, an_name='fmr', an_cost=0.00003, an_price=0.05)

# Добавляем запись
# session.add(fmr)  # добавить одну запись
# session.add_all([abc, xyz]) # Добавить несколько

# Удалить запис по фильтру
# f = session.query(Analysis).filter(Analysis.an_id == 1).one()
# session.delete(f)  # принимает объект и отмечает его как удаленный для следующего коммита

# Обновить одно значение
# i = session.get(Analysis, 1)  # получаем обьект по ключу
# i.an_name = "a3bc"     # новые данные
# session.add(i)

# Обновить несколько значений
k = session.query(Analysis2).filter(not_(Analysis2.an_name == "xyz")).update({Analysis2.an_cost: 2},
                                                                             synchronize_session=False)

# Благодаря этой строчке мы добавляем данные в таблицу
session.commit()

# print(session.query(Analysis.an_id, Analysis.an_name, Analysis.an_cost, Analysis.an_price).filter(
#     not_(Analysis.an_name == "xyz")).all())
# print(session.get(Analysis, 1))
# for res in session.query(Analysis):  # query создает select запрос в БД
#     print(res.an_id, res.an_name, res.an_cost, res.an_price)
