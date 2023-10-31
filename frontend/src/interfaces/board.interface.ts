export interface Board {
  id: number;
  title: string;
  image: unknown;
  candidates: CandidateProps[];
}

export interface CandidateProps {
  id: number;
  student: Student;
  kanban_position: number;
  score: number;
  notes: string;
  created_at: string;
  updated_at: string;
}

export interface Student {
  id: number;
  first_name: string;
  last_name: string;
  work_experience: string;
  image: unknown;
}
