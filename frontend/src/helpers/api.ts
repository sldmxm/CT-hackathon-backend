export type TPage = number | 'next' | 'prev';

class Api {
  #token =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxMTk1OTQwLCJpYXQiOjE2OTg2MDM5NDAsImp0aSI6IjAzNTZhYjZhNGQ4ZDQzODE5MTIxN2Q0MTc2NTZlM2RiIiwidXNlcl9pZCI6MX0.27VDMALGqCZf6FnCsW6QuUSmnE2zKrxK_UJG5xXecLI';
  constructor(public url: string) {
    this.url = url;
  }

  getVacancies() {
    return fetch(`${this.url}/vacancies/`, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.#token}`,
      },
    });
  }
  getVacancyById(id: string) {
    return fetch(`${this.url}/vacancies/${id}`, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.#token}`,
      },
    });
  }
  getCandidatesForBoard(id: string) {
    return fetch(`${this.url}/vacancies/${id}/candidates`, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.#token}`,
      },
    });
  }
  patchCandidate({
    candidateId,
    vacancyId,
    position,
  }: {
    candidateId: number;
    vacancyId: number;
    position: number;
  }) {
    return fetch(
      `${this.url}/vacancies/${vacancyId}/candidates/${candidateId}/`,
      {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.#token}`,
        },
        body: JSON.stringify({
          kanban_position: position,
        }),
      }
    );
  }

  async getCandidates() {
    const response = await fetch(`${this.url}/students/`, {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.#token}`,
      },
    });

    return response;
  }
}

export const api = new Api('http://130.193.36.223/api/v1');
