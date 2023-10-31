import { createAsyncThunk } from '@reduxjs/toolkit';

import { api } from '../../../../helpers/api';
import { Vacancy } from '../../../../interfaces/vacancy.interface';

export const fetchVacancies = createAsyncThunk(
  'vacancyList/fetchVacancies',
  async (_, { rejectWithValue }) => {
    const response = await api.getVacancies();
    if (!response.ok) {
      return rejectWithValue(response.statusText);
    }
    const vacancies: Vacancy[] = await response.json();

    return vacancies;
  }
);
