import { configureStore } from '@reduxjs/toolkit';
import {
  TypedUseSelectorHook,
  useDispatch,
  useSelector,
} from 'react-redux/es/exports';

import { candidatesReducer } from './candidates//slice';
import { boardReducer } from './features/board/slice';
import { vacanciesReducer } from './features/vacancies/slice';
import { vacancyReducer } from './features/vacancy/slice';

export const store = configureStore({
  reducer: {
    board: boardReducer,
    vacancies: vacanciesReducer,
    candidates: candidatesReducer,
    vacancy: vacancyReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
