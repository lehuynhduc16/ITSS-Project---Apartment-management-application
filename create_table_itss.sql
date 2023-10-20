-- Tạo cơ sở dữ liệu
CREATE DATABASE IF NOT EXISTS `itss`;

-- Sử dụng cơ sở dữ liệu vừa tạo
USE itss;

-- Tạo bảng building
CREATE TABLE building (
    building_id INT PRIMARY KEY,
    name VARCHAR(40),
    address VARCHAR(40),
    total_apartment INT
);

-- Tạo bảng apartment
CREATE TABLE apartment (
    apartment_id INT PRIMARY KEY,
    building_id INT,
    apartment_number INT,
    size INT,
    rent INT,
    FOREIGN KEY (building_id) REFERENCES building(building_id)
);

-- Tạo bảng tenant
CREATE TABLE tenant (
    tenant_id INT PRIMARY KEY,
    apartment_id INT,
    name VARCHAR(40),
    contact VARCHAR(40),
    status VARCHAR(40),
    FOREIGN KEY (apartment_id) REFERENCES apartment(apartment_id)
);

-- Tạo bảng contract
CREATE TABLE contract (
    contract_id INT PRIMARY KEY,
    tenant_id INT,
    start_date DATE,
    end_date DATE,
    notes VARCHAR(40),
    payment_amount INT,
    FOREIGN KEY (tenant_id) REFERENCES tenant(tenant_id)
);

-- Tạo bảng payment
CREATE TABLE payment (
    payment_id INT PRIMARY KEY,
    contract_id INT,
    payment_date DATE,
    amount INT,
    FOREIGN KEY (contract_id) REFERENCES contract(contract_id)
);

-- Tạo bảng user
CREATE TABLE user (
    user_id INT PRIMARY KEY,
    username VARCHAR(40),
    password VARCHAR(40),
    role VARCHAR(40)
);

-- Tạo bảng report
CREATE TABLE report (
    report_id INT PRIMARY KEY,
    name VARCHAR(40),
    description VARCHAR(40),
    status VARCHAR(40),
    create_by INT,
    FOREIGN KEY (create_by) REFERENCES user(user_id)
);

-- Tạo bảng reportResult
CREATE TABLE reportResult (
    result_id INT PRIMARY KEY,
    report_id INT,
    result_data JSON,
    FOREIGN KEY (report_id) REFERENCES report(report_id)
);

-- Tạo bảng scheduledReport
CREATE TABLE scheduledReport (
    schedule_id INT PRIMARY KEY,
    report_id INT,
    scheduled_time DATE,
    recipient VARCHAR(40),
    FOREIGN KEY (report_id) REFERENCES report(report_id)
);
