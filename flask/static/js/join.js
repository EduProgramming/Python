document.getElementById("join-btn").addEventListener("click", ({ target }) => {
  /** TODO: 작성 ID 유무 확인
   * 있다면True: 해결할 로직 작성
   * 없다면False: 비밀번호 확인 후에 문제가 없다면 CREATE
   *   - 비밀번호를 먼저 확인할 것인지 / ID유무를 먼저 확인할 것인지
   */
  const userPassword = document.getElementById("user-pwd");
  const userRePassword = document.getElementById("user-re-pwd");
  /**
   * TODO: 비밀번호가 다르다면 처리할 문구 작성
   * 해당 부분에 대해서는 가상 선택자로 처리할 거라서 수업내용과 무관
   */
  if (userPassword.value === userRePassword.value) {
    console.log("SAME");
  } else {
    console.log("NOOOP!");
  }
});
