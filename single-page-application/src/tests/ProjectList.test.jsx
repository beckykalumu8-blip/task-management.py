import { render, screen } from '@testing-library/react';
import ProjectList from './components/ProjectList';

const mockProjects = [
  { id: 1, title: 'Test Project', description: 'Test Desc', imageUrl: '', link: '' }
];

test('renders project list', () => {
  render(<ProjectList projects={mockProjects} />);
  const projectElement = screen.getByText(/Test Project/i);
  expect(projectElement).toBeInTheDocument();
});