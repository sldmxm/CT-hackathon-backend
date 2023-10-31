import { createAsyncThunk } from '@reduxjs/toolkit';

import { api } from '../../../../helpers/api';
import { Vacancy } from '../../../../interfaces/vacancy.interface';

export const fetchVacancy = createAsyncThunk(
  'vacancy/fetchVacancy',
  async (id: string, { rejectWithValue }) => {
    const response = await api.getVacancyById(id);
    if (!response.ok) {
      rejectWithValue(response.statusText);
    }
    const vacancy: Vacancy = await response.json();

    return vacancy;
  }
);
