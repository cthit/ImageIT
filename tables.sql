CREATE TABLE imageITTable(
    imageid UUID PRIMARY KEY,
    imagelink TEXT NOT NULL,
    userid UUID NOT NULL,
    uploadtime TIMESTAMP DEFAULT current_timestamp
);