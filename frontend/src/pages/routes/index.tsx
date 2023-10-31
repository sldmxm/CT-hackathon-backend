import { Suspense } from 'react';
import { RouteObject, createBrowserRouter } from 'react-router-dom';

import { Layout } from '../../layout';
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
        path: 'resumelist',
        element: <span></span>,
      },
    ],
  },
];

export const router = createBrowserRouter(routes);
