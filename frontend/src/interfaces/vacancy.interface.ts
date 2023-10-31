export interface Location {
  name: string;
}

export interface Grade {
  name: string;
}

export interface WorkSchedule {
  name: string;
}

export interface WorkFormat {
  name: string;
}

export interface HardSkill {
  name: string;
}

export interface CourseList {
  name: string;
}

export interface Vacancy {
  id: number;
  location: Location[];
  grade: Grade[];
  work_schedule: WorkSchedule[];
  work_format: WorkFormat[];
  course_list: CourseList[];
  hard_skill: HardSkill[];
  work_experience: string;
  education: string;
  office_format: string;
  specialty: string;
  image: string;
  title: string;
  description: string;
  salary_from: number;
  salary_to: number;
  company: string;
  is_active: boolean;
  is_published: boolean;
  created_at: string;
  updated_at: string;
  author: number;
}

export interface VacancyCardBodyProps
  extends Omit<Vacancy, 'title' | 'image'> {}
