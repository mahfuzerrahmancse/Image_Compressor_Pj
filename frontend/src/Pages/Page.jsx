import React, { useState } from "react";
import './Page.css'

export const Page = () => {
  const [file, setFile] = useState(null);
  const [compressedImageUrl, setCompressedImageUrl] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("http://localhost:5000/compress_image", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const compressedImageName = await response.json();
        const compressedUrl = `http://localhost:5000/images/${compressedImageName}`;
        setCompressedImageUrl(compressedUrl);
      } else {
        // Handle error
        console.error("Error compressing image");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          padding: "20px",
          background: "#f0f0f0",
          alignItems: "center",
          gap: "10px",
        }}
      >
        <input
          type="file"
          style={{
            padding: "10px",
            background: "#f0f0f0",
            border: "1px solid black",
            borderRadius: "10px",
          }}
          onChange={handleFileChange}
        />
        <button
          style={{
            padding: "15px",
            background: "green",
            border: "none",
            color: "white",
            borderRadius: "10px",
            cursor: "pointer",
            fontSize:"16px",
          }}
          onClick={handleUpload}
        >
          Compress
        </button>
      </div>
      <div style={{ display: "flex" }}>
        {file && (
          <div style={{ width: "50%", padding: "20px" }}>
            <p>Original Image:</p>
            <img
              style={{ width: "100%" }}
              src={URL.createObjectURL(file)}
              alt="Compressed"
            />
          </div>
        )}
        {compressedImageUrl && (
          <div style={{ width: "50%", padding: "20px" }}>
            <p>Compressed Image:</p>
            <img
              style={{ width: "100%" }}
              src={compressedImageUrl}
              alt="Compressed"
            />
          </div>
        )}
      </div>
    </div>
  );
};
