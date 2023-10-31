import { PayloadAction, createSlice } from '@reduxjs/toolkit';

import { fetchCandidatesForBoard } from './thunk/fetchCandidatesForBoard';

import { patchCandidateInfo } from './thunk/patchCandidateInfo';

import { Board } from '../../../interfaces/board.interface';
import { Status } from '../../../interfaces/status';

interface InitialState {
  board: ReadonlyArray<Board>;
  status: Status;
}

const initialState: InitialState = {
  board: [],
  status: Status.Idle,
};

const boardSlice = createSlice({
  name: 'board',
  initialState,
  reducers: {
    moveCandidate: (
      state,
      action: PayloadAction<{ id: number; position: number }>
    ) => {
      const { id, position } = action.payload;
      const candidate = state.board[0].candidates.find(
        (item) => item.id === id
      );
      if (candidate) {
        candidate.kanban_position = position;
      }
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchCandidatesForBoard.pending, (state) => {
        state.status = Status.Pending;
      })
      .addCase(fetchCandidatesForBoard.fulfilled, (state, action) => {
        state.status = Status.Success;
        state.board = action.payload;
      })
      .addCase(fetchCandidatesForBoard.rejected, (state) => {
        state.status = Status.Failed;
      })
      .addCase(patchCandidateInfo.pending, (state) => {
        state.status = Status.Pending;
      })
      .addCase(patchCandidateInfo.fulfilled, (state) => {
        state.status = Status.Success;
      })
      .addCase(patchCandidateInfo.rejected, (state) => {
        state.status = Status.Failed;
      });
  },
});
export const { moveCandidate } = boardSlice.actions;
export const boardReducer = boardSlice.reducer;
