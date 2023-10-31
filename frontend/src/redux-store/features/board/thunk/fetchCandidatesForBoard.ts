import { createAsyncThunk } from '@reduxjs/toolkit';

import { api } from '../../../../helpers/api';
import { Board } from '../../../../interfaces/board.interface';

export const fetchCandidatesForBoard = createAsyncThunk(
  'boardCandidates/fetchCandidatesForBoard',
  async (id: string, { rejectWithValue }) => {
    const response = await api.getCandidatesForBoard(id);
    if (!response.ok) {
      rejectWithValue(response.status);
    }
    const candidatesBoard: Board[] = await response.json();

    return candidatesBoard;
  }
);
