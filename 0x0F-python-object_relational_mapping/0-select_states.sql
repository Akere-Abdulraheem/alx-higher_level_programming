-- a

create database if not exists hbtn_0e_0_usa;
use hbtn_0e_0_usa;
create table if not exists states (
		id INT NOT NULL AUTO_INCREMENT,
		name VARCHAR(256) NOT NULL,
		PRIMARY KEY (id)
		);

insert into states (name) values ("California"), 
  ("Arizona"), ("Texas"), 
  ("New York"), ("Nevada");
