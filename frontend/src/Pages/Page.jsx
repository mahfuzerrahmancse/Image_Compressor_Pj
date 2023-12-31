import React, { useState } from "react";
import styles from "./Page.module.css";

export const Page = () => {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageChange = (event) => {
    const image = event.target.files[0];
    if (image.size < 2000000) {
      const reader = new FileReader();
      reader.onload = () => {
        setSelectedImage(reader.result);
      };
      reader.readAsDataURL(image);
    } else {
      alert("Image size more than 2MB");
    }
  };

  const handleSelectImageClick = () => {
    document.getElementById("file").click();
  };

  return (
    <div className={styles.container}>
      <input
        type="file"
        id="file"
        accept="image/*"
        hidden
        onChange={handleImageChange}
      />
      <div
        className={`${styles["img-area"]} ${
          selectedImage ? styles.active : ""
        }`}
        data-img={selectedImage ? "image" : ""}
      >
        {!selectedImage && (
          <>
            <i
              className={`bx bxs-cloud-upload ${styles.icon}`}
              style={{ fontSize: "100px" }}
            ></i>
            <h3>Upload Image</h3>
            <p>
              Image size must be less than <span>2MB</span>
            </p>
          </>
        )}
        {selectedImage && <img src={selectedImage} alt="Preview" />}
      </div>
      <button className={styles.selectImage} onClick={handleSelectImageClick}>
        Select Image
      </button>
    </div>
  );
};
