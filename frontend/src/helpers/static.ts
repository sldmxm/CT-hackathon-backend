import { ViewVariant } from '../components/ui/components/Badge/component';

export const titles = [
  'Компания',
  'Формат',
  'Регион',
  'График',
  'Опыт работы',
  'Тип занятости',
  'Портфолио',
  'Язык',
  'Грейд',
  'Навыки',
  'Дополнительно',
];

export const matchHash: Record<string, string> = {
  Компания: 'company',
  Формат: 'office_format',
  Регион: 'location',
  График: 'work_schedule',
  'Опыт работы': 'work_experience',
  'Тип занятости': 'work_format',
  Портфолио: 'portfolio',
  Язык: 'language_level',
  Грейд: 'grade',
  Навыки: 'hard_skill',
  Дополнительно: 'description',
};

export const columnTitle: ViewVariant[] = [
  'Кандидаты',
  'Тестовое',
  'Собеседование',
  'Офер',
  'Отказ',
  'Резерв',
];

export const navVacancyLabes: string[] = ['Новые кандидаты', 'Моя доска'];
