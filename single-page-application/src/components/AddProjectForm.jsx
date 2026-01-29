import React, { useState } from 'react';

function AddProjectForm({ addProject }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [link, setLink] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title && description) {
      addProject({ title, description, imageUrl, link });
      setTitle('');
      setDescription('');
      setImageUrl('');
      setLink('');
    }
  };

  return (
    <form className="add-project-form" onSubmit={handleSubmit}>
      <h2>Add New Project</h2>
      <input
        type="text"
        placeholder="Project Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      <textarea
        placeholder="Project Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        required
      />
      
      <button type="submit">Add Project</button>
    </form>
  );
}

export default AddProjectForm;