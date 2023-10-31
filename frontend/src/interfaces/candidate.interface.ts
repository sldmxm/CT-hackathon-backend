import {
  CourseList,
  HardSkill,
  WorkFormat,
  WorkSchedule,
  Location,
} from './vacancy.interface';

export interface OfficeFormat {
  name: string;
}

export interface Candidate {
  id: number;
  course_list: CourseList[];
  hard_skills: HardSkill[];
  image: string;
  first_name: string;
  last_name: string;
  email: string;
  telegram_username: string;
  salary_from: number;
  portfolio_link: string;
  resume_link: string;
  activity_level: number | null;
  created_at: string;
  updated_at: string;
  education: string;
  status: string;
  work_experience: string;
  current_location: string;
  location_to_relocate: Location[];
  specialty: string;
  work_schedule: WorkSchedule[];
  work_format: WorkFormat[];
  office_format: OfficeFormat[];
}
