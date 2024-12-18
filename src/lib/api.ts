const API_BASE_URL = 'http://localhost:8000'; // Update with your actual API URL

export async function generateReport(data: ReportRequest): Promise<ReportResponse> {
  const response = await fetch(`${API_BASE_URL}/generate-report`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      government_level: data.governmentLevel,
      province: data.province,
      report_type: data.reportType,
      user_name: data.userName,
      company_email: data.email,
    }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message || 'Failed to generate report');
  }

  return response.json();
}