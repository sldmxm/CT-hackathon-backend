import { createAsyncThunk } from '@reduxjs/toolkit';

import { api } from '../../../helpers/api';
import { Candidate } from '../../../interfaces/candidate.interface';

export const fetchCandidates = createAsyncThunk(
  'candidatesList/fetchCandidates',
  async (_, { rejectWithValue }) => {
    const response = await api.getCandidates();
    if (!response.ok) {
      return rejectWithValue(response.statusText);
    }
    const res = await response.json();
    const candidates: Candidate[] = res.results;

    return candidates;
  }
);
