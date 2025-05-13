-- Airbnb Database
-- Description: This SQL script creates a MySQL database for an Airbnb-like system, managing users, properties, bookings, payments, reviews, and messages.
-- Created for Week 8 Assignment: Build a Complete Database Management System
-- Specification: Implements six entities with one-to-many relationships, using UUIDs for primary keys and appropriate constraints.

-- Create the User table to store host, guest, and admin details
CREATE TABLE User (
    user_id CHAR(32) PRIMARY KEY, -- UUID stored as CHAR(32)
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    role ENUM('guest', 'host', 'admin') NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(email), -- Ensure email is unique
    INDEX(user_id) -- Index on primary key for performance
);

-- Create the Property table to store property listings
CREATE TABLE Property (
    property_id CHAR(32) PRIMARY KEY, -- UUID stored as CHAR(32)
    host_id CHAR(32) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(255) NOT NULL,
    pricepernight DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (host_id) REFERENCES User(user_id) ON DELETE RESTRICT, -- Prevent deletion if user has properties
    INDEX(property_id), -- Index on primary key
    CHECK (pricepernight > 0) -- Ensure price is positive
);

-- Create the Booking table to store reservation details
CREATE TABLE Booking (
    booking_id CHAR(32) PRIMARY KEY, -- UUID stored as CHAR(32)
    property_id CHAR(32) NOT NULL,
    user_id CHAR(32) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'confirmed', 'canceled') NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES Property(property_id) ON DELETE RESTRICT, -- Prevent deletion if property has bookings
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE RESTRICT, -- Prevent deletion if user has bookings
    INDEX(booking_id), -- Index on primary key
    CHECK (end_date > start_date), -- Ensure end date is after start date
    CHECK (total_price >= 0) -- Ensure total price is non-negative
);

-- Create the Payment table to store payment details for bookings
CREATE TABLE Payment (
    payment_id CHAR(32) PRIMARY KEY, -- UUID stored as CHAR(32)
    booking_id CHAR(32) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'paypal', 'stripe') NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id) ON DELETE CASCADE, -- Delete payments if booking is deleted
    INDEX(payment_id), -- Index on primary key
    CHECK (amount > 0) -- Ensure payment amount is positive
);

-- Create the Review table to store guest reviews for properties
CREATE TABLE Review (
    review_id CHAR(32) PRIMARY KEY, -- UUID stored as CHAR(32)
    property_id CHAR(32) NOT NULL,
    user_id CHAR(32) NOT NULL,
    rating INTEGER NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES Property(property_id) ON DELETE CASCADE, -- Delete reviews if property is deleted
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE, -- Delete reviews if user is deleted
    INDEX(review_id), -- Index on primary key
    CHECK (rating >= 1 AND rating <= 5) -- Ensure rating is between 1 and 5
);

-- Create the Message table to store communication between users
CREATE TABLE Message (
    message_id CHAR(32) PRIMARY KEY, -- UUID stored as CHAR(32)
    sender_id CHAR(32) NOT NULL,
    recipient_id CHAR(32) NOT NULL,
    message_body TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES User(user_id) ON DELETE CASCADE, -- Delete messages if sender is deleted
    FOREIGN KEY (recipient_id) REFERENCES User(user_id) ON DELETE CASCADE, -- Delete messages if recipient is deleted
    INDEX(message_id) -- Index on primary key
);
