
(setq rpm-input-method "devanagari-itrans")

(defun rpm-apply-input-method ()
  "buffer to buffer apply input method with buffering windowing stuff mixed up"
  (interactive)
  (let* ((inp (buffer-substring-no-properties (point-min) (point-max)))
	 (filename (file-name-nondirectory (buffer-file-name)))
	 (outname (concat (file-name-sans-extension filename)
			       "-hi"
			       (file-name-extension filename t)))
	 (p))
    (switch-to-buffer-other-frame outname)
    (save-excursion
      (save-window-excursion
	(setq buffer-file-coding-system 'utf-8)
	(set-input-method rpm-input-method t)
	(setq p (point))
	(erase-buffer)
	(execute-kbd-macro inp)))
    (goto-char p)
    (other-frame 1)))

(global-set-key [f4] 'rpm-apply-input-method)

;(run-with-idle-timer 5 t 'rpm-apply-input-method)
