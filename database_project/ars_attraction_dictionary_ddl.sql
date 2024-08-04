create table ars_attraction_dictionary
(
    pk_attraction_dictionary_id int auto_increment primary key,
    attraction_name NVARCHAR(64) not null,
    is_in_use int not null DEFAULT '1',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);