import React from 'react';

import { useParams } from 'react-router-dom';

import { VacancyCard } from './component';

import { fetchCandidatesForBoard } from '../../redux-store/features/board/thunk/fetchCandidatesForBoard';
import { selecetVacancyModule } from '../../redux-store/features/vacancy/selector';
import { fetchVacancy } from '../../redux-store/features/vacancy/thunk/fetchVacancy';
import { useAppDispatch, useAppSelector } from '../../redux-store/store';

export function VacancyCardContainer() {
  const { id } = useParams();
  const dispatch = useAppDispatch();
  const { vacancy } = useAppSelector(selecetVacancyModule);

  React.useEffect(() => {
    Promise.all([
      dispatch(fetchVacancy(id!)),
      dispatch(fetchCandidatesForBoard(id!)),
    ]);
  }, [dispatch, id]);

  if (!vacancy) {
    return;
  }

  return <VacancyCard vacancy={vacancy} />;
}
