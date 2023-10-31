import { PayloadAction, createSlice } from '@reduxjs/toolkit';

import { fetchVacancy } from './thunk/fetchVacancy';

import { Status } from '../../../interfaces/status';
import { Vacancy } from '../../../interfaces/vacancy.interface';

interface InitialState {
  status: Status;
  vacancy: Vacancy | null;
}

const initialState: InitialState = {
  status: Status.Idle,
  vacancy: null,
};

const vacancySlice = createSlice({
  name: 'vacancyList',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchVacancy.pending, (state) => {
        state.status = Status.Pending;
      })
      .addCase(
        fetchVacancy.fulfilled,
        (state, action: PayloadAction<Vacancy>) => {
          state.status = Status.Success;
          state.vacancy = action.payload;
        }
      )
      .addCase(fetchVacancy.rejected, (state) => {
        state.status = Status.Failed;
      });
  },
});

export const vacancyReducer = vacancySlice.reducer;
