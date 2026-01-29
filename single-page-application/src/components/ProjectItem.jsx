import React from 'react';

function ProjectItem({ project }) {
  return (
    <div className="project-item">
      <img src={project.imageUrl} alt={project.title} />
      <h3>{project.title}</h3>
      <p>{project.description}</p>
      <a href={project.link} target="_blank" rel="noopener noreferrer">View Project</a>
    </div>
  );
}

export default ProjectItem;