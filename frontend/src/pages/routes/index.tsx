import { Suspense } from 'react';
import { RouteObject, createBrowserRouter } from 'react-router-dom';

import { Layout } from '../../layout';
import { CandidatesPage } from '../Candidates';
import { MainPageVacancy } from '../MainPageVacancy';
import { VacancyPage } from '../VacancyPage';

const routes: RouteObject[] = [
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        index: true,
        element: (
          <Suspense fallback={<>Загрузка...</>}>
            <MainPageVacancy />
          </Suspense>
        ),
      },
      {
        path: '/vacancy/:id',
        element: <VacancyPage />,
      },
      {
        path: 'candidates',
        element: <CandidatesPage />,
      },
    ],
  },
];

export const router = createBrowserRouter(routes);
