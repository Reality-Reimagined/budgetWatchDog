export interface ReportRequest {
  governmentLevel: 'federal' | 'provincial';
  province?: string;
  reportType: 'financial' | 'economic' | 'demographic';
  userName: string;
  email: string;
}

export interface ReportResponse {
  filePath: string;
  graphs: string[];
  tables: {
    [key: string]: string;
  }[];
}

export interface FinancialMetrics {
  gdpGrowth: number;
  debtToGDP: number;
  employmentRate: number;
  deficit: number;
  revenue: number;
  expenses: number;
}

export interface ApiError {
  message: string;
  status: number;
}