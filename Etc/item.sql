# create table 'item' for jing dong

CREATE TABLE item 
(
    time        datetime,
    item_id     varchar(31),
    item_name   varchar(255),
    price       float(10,2),
    in_stock    smallint
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
