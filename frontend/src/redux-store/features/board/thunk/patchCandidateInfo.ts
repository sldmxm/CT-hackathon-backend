import { createAsyncThunk } from '@reduxjs/toolkit';

import { api } from '../../../../helpers/api';

export const patchCandidateInfo = createAsyncThunk(
  'patchCandidate',
  async (
    {
      candidateId,
      vacancyId,
      position,
    }: {
      candidateId: number;
      vacancyId: number;
      position: number;
    },
    { rejectWithValue }
  ) => {
    const response = await api.patchCandidate({
      candidateId,
      vacancyId,
      position,
    });

    if (!response.ok) {
      rejectWithValue(response.status);
    }
    return await response.json();
  }
);
