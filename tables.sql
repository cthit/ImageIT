CREATE TABLE imageITTable(
    imageid UUID PRIMARY KEY,
    imagelink TEXT NOT NULL,
    userid UUID NOT NULL,
    uploadTime TIMESTAMP DEFAULT current_timestamp 
);