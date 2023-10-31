import {
  PayloadAction,
  createEntityAdapter,
  createSlice,
} from '@reduxjs/toolkit';

import { fetchCandidates } from './thunk/fetchCandidates';

import { Candidate } from '../../interfaces/candidate.interface';
import { Status } from '../../interfaces/status';

const candidatesEntityAdapter = createEntityAdapter<Candidate>();

const candidatesSlice = createSlice({
  name: 'candidatesList',
  initialState: candidatesEntityAdapter.getInitialState({
    status: Status.Idle,
  }),
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchCandidates.pending, (state) => {
        state.status = Status.Pending;
      })
      .addCase(
        fetchCandidates.fulfilled,
        (state, action: PayloadAction<Candidate[]>) => {
          state.status = Status.Success;
          candidatesEntityAdapter.setAll(state, action.payload);
        }
      )
      .addCase(fetchCandidates.rejected, (state) => {
        state.status = Status.Failed;
      });
  },
});

export const candidatesReducer = candidatesSlice.reducer;
export const { selectAll } = candidatesEntityAdapter.getSelectors();
