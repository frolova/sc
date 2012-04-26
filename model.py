# -*- coding: utf-8 -*-

import datetime
import logging

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, scoped_session, create_session, backref, relationship, relation
from sqlalchemy import Table, Column, Integer, Float, String, Date, MetaData, Boolean, String
from sqlalchemy.ext.associationproxy import association_proxy

from datetime import date

Base = declarative_base()

engine = create_engine('sqlite:///base.db', echo=True)
Session = scoped_session(sessionmaker(bind=engine))
query_session = Session()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    male = Column(Boolean,default=True)
    birthday = Column(Date, nullable=False)
    phone = Column(String, nullable=False)

    def get_fio(self):
        return '%s %s %s'%(self.surname, self.name, self.lastname)

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    position_id = Column(Integer, ForeignKey('positions.id'), nullable=False)
    login = Column(String, nullable=False)
    passwd = Column(String, nullable=False)

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(Integer, nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    manager_id = Column(Integer, ForeignKey('staff.id'), nullable=False)
    client_id = Column(Integer,  ForeignKey('clients.id'), nullable=False)
    device = Column(String, nullable=False)
    description = Column(String, nullable=False)

    def get_client(self):
        s = Session()
        return s.query(Client).filter_by(id=self.client_id).one()

    def get_status(self,flag):
        #flag: 0 - min; 1 - max, 2 - all
        s = Session()
        statuses = s.query(Status).filter_by(id=self.id).all()
        s.close()

        if flag == 0:
            min_stat = statuses[0]
            for stat in statuses:
                if min_stat.status < stat.status:
                    min_stat = stat
            return min_stat
        elif flag == 1:
            max_stat = statuses[0]
            for stat in statuses:
                if max_stat.status > stat.status:
                    max_stat = stat
            return max_stat
        return statuses
    def get_ordered_date(self):
        return self.get_status(0).date

    def __init__(self):
        s = Session()
        status = Status()
        status.order = self.id
        status.date = date.today()
        status.status = 0
        status.order_id = next_id(Order)
        s.add(status)
        s.commit()
        s.close()

class Status(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Integer, nullable=False)

    def to_string(self):
        if self.status == 0:
            return 'Принят в ремонт'

Base.metadata.create_all(engine)


def next_id(tbl):
    s = Session()
    id = s.query(func.max(tbl.id)).one()
    if (id[0]):
        return int(id[0]) + 1
    else:
        return 0

# s = Session()
# p = Position()
# p.name = 'Manager'
# p.permissions = 777
# s.add(p)
# s.commit()
# m = Staff()
# m.name = 'Ivan'
# m.lastname = 'Ivanovich'
# m.surname = 'Ivanov'
# m.position_id = p.id
# m.login = 'ivan'
# m.passwd = '123'
# s.add(m)
# s.commit()
# s.close()