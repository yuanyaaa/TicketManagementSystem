drop table if exists refund;
create table refund(
    rf_tcid char(9),
    rf_time date,
    rf_money float
);


alter table departuretime drop foreign key departuretime_ibfk_1;
alter table departuretime drop foreign key departuretime_ibfk_2;

drop table if exists station;
create table station(
    s_sid        char(9),
    s_sname      varchar(40) null,
    s_slongitude float       null,
    s_slatitude  float       null,
    primary key(s_sid)
);

drop table if exists ticket;
create table ticket
(
    tc_tcid     char(9)    primary key,
    tc_date     date       null,
    tc_trainnum char(9)    null,
    tc_aimsid   char(9)    null,
    tc_price    float      null,
    tc_seatnum  int        null,
    tc_cid      char(9)    null,
    tc_ifrefund tinyint(1) null,
    tc_custid   char(18)   null
);

drop table if exists train;
create table train(
    t_tid     char(9) primary key,
    t_ttype   char(8) null,
    t_seatnum int     null
);

drop table if exists conductor;
create table conductor(
    c_cid       char(9)     primary key,
    c_cname     varchar(40) null,
    c_cpassword varchar(40) null
);

drop table if exists manager;
create table manager
(
    m_mid       char(9)     primary key,
    m_mname     varchar(40) null,
    m_mpassword varchar(40) null
);



drop table if exists departuretime;
create table departuretime
(
    dt_trainnum       char(9),
    dt_aimsid         char(9) null,
    dt_tid            char(9) null,
    dt_departuretime  datetime    null,
    dt_month          int     null,
    dt_date           int     null,
    dt_ticketentrance int     null,
    dt_cost           int     null,
    primary key (dt_trainnum),
    foreign key (dt_aimsid) references station(s_sid),
    foreign key (dt_tid) references train(t_tid)
);



drop trigger if exists insert_c;
delimiter $$
create trigger insert_c before insert on TicketManagementSystem.conductor for each row
begin
    declare
	tmp character(9);
    select max(c_cid) into tmp from conductor;
     if (tmp is null)
    then set tmp = 0;
    end if;
	set tmp = tmp + 1;
    set NEW.c_cid = tmp;
end$$
delimiter ;
# insert into conductor values(20, 'wssss', '666666');
# select * from conductor;

drop trigger if exists insert_m;
delimiter $$
create trigger insert_m before insert  on manager for each row
begin
    declare tmp character(9) default 0;
    select max(m_mid) into tmp from manager;
    if (tmp is null)
    then set tmp = 0;
    end if;
	set tmp = tmp + 1;
    set NEW.m_mid = tmp;
end$$
delimiter ;
delete from manager where m_mid is null ;
# insert into manager values(10, 'ws', '666666');
# select * from manager;

# drop trigger if exists insert_s;
# delimiter $$
# create trigger insert_s before insert  on station for each row
# begin
#     declare tmp character(9) default 0;
#     select max(s_sid) into tmp from station;
#     if (tmp is null)
#     then set tmp = 0;
#     end if;
#
#     if(NEW.s_sname is null)
#     then set NEW.s_sname = 'default';
#     end if;
#
# 	set tmp = tmp + 1;
#     set NEW.s_sid = tmp;
# end$$
# delimiter ;

#insert into station(s_slongitude, s_slatitude) values(100, 200);
#select * from station;

drop trigger if exists insert_m;
delimiter $$
create trigger insert_m before insert  on ticket for each row
begin
    declare tmp character(9) default 0;
    select max(tc_tcid) into tmp from ticket;
    if (tmp is null)
    then set tmp = 0;
    end if;
	set tmp = tmp + 1;
    set NEW.tc_tcid = tmp;
end$$
delimiter ;

drop procedure if exists refundticket;
delimiter $$
create procedure  refundticket(tcid char(9), money float)
begin
    declare ddate date;
    select current_date into ddate;
    update ticket set tc_ifrefund = true where tc_tcid = tcid;
    insert into refund(rf_tcid, rf_time, rf_money) values (tcid, ddate, money);
end$$
delimiter ;

# drop procedure if exists searchcredit;
# delimiter $$
# create procedure searchcredit(credit character(18),
#                                 out ddate date,
#                                 out trainnum character(9),
# 								out aimsname character varying,
# 								out price double precision,
# 								out seatnum smallint,
# 								out tcid character(9))
# begin
#     declare rec varchar(45);
#     select tc_tcid, tc_date, tc_trainnum, s_sname, tc_price, tc_seatnum from ticket, station
# 	where tc_aimsid = s_sid and tc_custid = credit and tc_ifrefund = false;
#     loop
# 		set ddate = rec.tc_date;
# 		set trainnum = rec.tc_trainnum;
# 		set aimsname = rec.s_sname;
# 		set price = rec.tc_price;
# 		set seatnum = rec.tc_seatnum;
# 		set tcid = rec.tc_tcid;
# 	end loop;
# end $$
# delimiter ;

drop procedure if exists sellticket;
delimiter $$
create procedure sellticket(num smallint,
                            trainnum char(9),
                            s_date varchar(45),
							aimsname varchar(45),
							price float,
							cname char(9),
							custid char(18))

begin
declare idcnt integer;
declare i smallint;
declare aimsid character(9);
declare cid character(9);
declare seatnum smallint;
	set i = 0;
	select s_sid into aimsid from station where s_sname = aimsname;
	select c_cid into cid from conductor where c_cname = cname;
	select count(*) into idcnt from ticket;
	while i < num do
		set idcnt = idcnt + 1 ;
		select max(tc_seatnum) into seatnum from ticket where tc_trainnum = trainnum;
		if seatnum is NULL
		then
			set seatnum = 0;
		end if;
		set seatnum = seatnum + 1;
		insert into ticket(tc_tcid, tc_date, tc_trainnum,tc_aimsid, tc_price, tc_seatnum, tc_cid, tc_custid)
						  values(idcnt, cast(s_date as date), trainnum, aimsid,
								price, seatnum, cid, custid);
		set i = i + 1;
    end while;
end$$