import { render, screen, fireEvent } from '@testing-library/react';
import AddProjectForm from './components/AddProjectForm';

test('adds a project', () => {
  const mockAddProject = jest.fn();
  render(<AddProjectForm addProject={mockAddProject} />);
  
  fireEvent.change(screen.getByPlaceholderText(/Project Title/i), { target: { value: 'New Project' } });
  fireEvent.change(screen.getByPlaceholderText(/Project Description/i), { target: { value: 'New Desc' } });
  fireEvent.click(screen.getByText(/Add Project/i));
  
  expect(mockAddProject).toHaveBeenCalledWith({
    title: 'New Project',
    description: 'New Desc',
    imageUrl: '',
    link: ''
  });
});