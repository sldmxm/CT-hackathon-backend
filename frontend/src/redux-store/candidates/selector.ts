import { selectAll } from './slice';

import { RootState } from '../store';

export const selectCandidatesModule = (state: RootState) =>
  selectAll(state.candidates);
