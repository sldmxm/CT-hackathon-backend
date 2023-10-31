import {
  ResumeIcon,
  VacancyIcon,
  VacancyIconActive,
} from '../components/ui/icons';
import { ResumeIconActive } from '../components/ui/icons/ResumeIconActive';

export const navRoutes = [
  {
    path: '',
    icon: {
      active: VacancyIconActive,
      unactive: VacancyIcon,
    },
  },
  {
    path: 'candidates',
    icon: {
      active: ResumeIconActive,
      unactive: ResumeIcon,
    },
  },
] as const;
