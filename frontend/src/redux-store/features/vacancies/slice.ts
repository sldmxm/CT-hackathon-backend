import { PayloadAction, createSlice } from '@reduxjs/toolkit';

import { fetchVacancies } from './thunk/fetchVacancies';

import { Status } from '../../../interfaces/status';
import { Vacancy } from '../../../interfaces/vacancy.interface';

interface InitialState {
  status: Status;
  vacancies: Vacancy[];
}

const initialState: InitialState = {
  status: Status.Idle,
  vacancies: [],
};

const vacanciesSlice = createSlice({
  name: 'vacancyList',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchVacancies.pending, (state) => {
        state.status = Status.Pending;
      })
      .addCase(
        fetchVacancies.fulfilled,
        (state, action: PayloadAction<Vacancy[]>) => {
          state.status = Status.Success;
          state.vacancies = action.payload;
        }
      )
      .addCase(fetchVacancies.rejected, (state) => {
        state.status = Status.Failed;
      });
  },
});

export const vacanciesReducer = vacanciesSlice.reducer;
