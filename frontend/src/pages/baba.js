import React, { useState } from "react";

function ImageUploadForm() {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setSelectedImage(file);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Here, you can send 'selectedImage' to your server or perform any other action.
    if (selectedImage) {
      const formData = new FormData();
      formData.append("image", selectedImage);

      // Example: Sending the image to an API endpoint
      fetch("/api/upload", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Image uploaded successfully!", data);
        })
        .catch((error) => {
          console.error("Error uploading image:", error);
        });
    } else {
      console.log("No image selected.");
    }
  };

  let createUser = async (user) => {
    fetch(`/api/users/create/`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    })       
}

  return (
    <div>
      <h2>Image Upload Form</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="image">Select an image:</label>
          <input
            type="file"
            id="image"
            name="image"
            accept="image/*" // Specify accepted file types
            onChange={handleImageChange}
          />
        </div>
        <div>
          <button type="submit">Upload Image</button>
        </div>
      </form>
    </div>
  );
}

export default ImageUploadForm;
