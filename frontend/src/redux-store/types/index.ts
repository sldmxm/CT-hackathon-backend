import { createAsyncThunk } from '@reduxjs/toolkit';

import { RootState, AppDispatch } from '../store';

export type ThunkApiConfig = {
  state: RootState;
  dispatch: AppDispatch;
  rejectValue: string;
  extra: { s: string; n: number };
};

export const createAppAsyncThunk = createAsyncThunk.withTypes<ThunkApiConfig>();
